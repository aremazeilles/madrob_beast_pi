#!/usr/bin/env python
# coding=utf-8

import yaml
from os import path
from sys import argv, exit
from datetime import datetime

import pandas as pd


def performance_indicator(preprocessed_filenames_dict, condition, output_dir, start_time):

    door_occupation_time = 'TIMEOUT'

    events_df = pd.read_csv(preprocessed_filenames_dict['event'], skipinitialspace=True)

    if condition['robot_approach_side'] == 'CW':
        approach_side = 'cw'
        destination_side = 'ccw'
    else:
        approach_side = 'ccw'
        destination_side = 'cw'

    # Check if the robot has moved to the destination side
    robot_moves_to_dest_events = events_df.loc[events_df['event'] == 'humanoid_moves_to_{}_side'.format(destination_side)]
    if len(robot_moves_to_dest_events) > 0:
        robot_moves_to_dest = robot_moves_to_dest_events.iloc[0]

        # Check if the robot approach event exists
        robot_approach_events = events_df.loc[events_df['event'] == 'humanoid_approaches_the_door_on_{}_side'.format(approach_side)]
        if len(robot_approach_events) > 0:
            robot_approach = robot_approach_events.iloc[0]

            # Check if 'robot moves to destination' occurs after 'robot approaches the door'
            if robot_moves_to_dest['time'] > robot_approach['time']:
                door_occupation_time = float(robot_moves_to_dest['time']) - float(robot_approach['time'])

    # Write result yaml file
    filepath = path.join(output_dir, 'door_occupation_time.yaml')
    with open(filepath, 'w+') as result_file:
        yaml.dump({
            'type': 'scalar',
            'value': door_occupation_time,
        }, result_file, default_flow_style=False)


def run_pi(event_path, condition_path, output_folder_path):
    with open(condition_path, 'r') as condition_file:
        condition_dict = yaml.safe_load(condition_file)

    performance_indicator({'event': event_path}, condition_dict, output_folder_path, datetime.now())
    return 0


if __name__ == '__main__':
    arg_len = 4
    script_name = 'door_occupation_time'
    if len(argv) != arg_len:
        print "[Performance Indicator {script_name}] Error: arguments must be {script_name}.py event.csv condition.yaml output_dir".format(script_name=script_name)
        exit(-1)

    event_path, condition_path, output_folder_path = argv[1:]

    run_pi(event_path, condition_path, output_folder_path)