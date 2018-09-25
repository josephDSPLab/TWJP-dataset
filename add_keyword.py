import os
import numpy as np
from ruamel import yaml


def pull_keyword(prop, keyword):
    if (prop != 'location_KW') and (prop != 'soundsource_KW'):
        print('Unsupported property: ',prop)
        return
    if not isinstance(keyword, str):
        print('Added keyword should be a valid string!')
        return
    with open('metadata.yaml', 'r') as stream:
        org_dict = yaml.load(stream, Loader=yaml.RoundTripLoader)
    if prop in org_dict:
        if isinstance(org_dict[prop],yaml.comments.CommentedSeq):
            if str(keyword) not in org_dict[prop]:
                org_dict[prop].append(str(keyword))
        else:
            org_dict[prop] = [str(keyword)]
    else:
        org_dict[prop] = [str(keyword)]
    change_dump = yaml.dump(
        org_dict, default_flow_style=False, Dumper=yaml.RoundTripDumper)
    with open('metadata.yaml', 'w') as stream:
        stream.write(change_dump)
    return
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser('Add new keyword in metadata')
    parser.add_argument('property',metavar='prop',type=str)
    parser.add_argument('new_keyword',metavar='new_KW',type=str)
    args = parser.parse_args()
    pull_keyword(args.property, args.new_keyword)


