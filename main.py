import yaml


python_version = 'python2.7'
ignored_stages = True
new_stages = []
replaceMakesBy = 'build.py'
inputFile = 'gitlab-ci.yml'
outputFile = 'new-gitlab-ci.yml'


def addNewStages(stages):
    global new_stages
    for stage in new_stages:
        stages.append(stage)


def changePythonVersion(to_version=python_version):
    return to_version


def removeMakes(yml_dict):
    r''' removes all makes in the yaml file '''
    # print(yml_dict)
    # print('------------------')
    if type(yml_dict) == str and 'make' in yml_dict:
        # print('                   ****************')
        # print('                   **** M A K E ***')
        # print('                   ****************')
        yml_dict.replace('make', replaceMakesBy)

    elif type(yml_dict) == type(dict()):
        for i, (key, value) in enumerate(yml_dict.items()):
            # print('++++++++++++++++++')
            # print('key in dic', key)
            # print('value in dic', value)
            # print('++++++++++++++++++')
            if type(value) == str and 'make' in value:
                # print('                   ****************')
                # print('                   **** M A K E ***')
                # print('                   ****************')
                yml_dict[key] = value.replace('make', replaceMakesBy)
            else:
                removeMakes(value)

            # print('key', key, 'value', value)
    elif type(yml_dict) == type(list()):
        for i, value in enumerate(yml_dict):
            # print('++++++++++++++++++')
            # print('i list', i)
            # print('value in list', value)
            # print('++++++++++++++++++')
            if type(value) == str and 'make' in value:
                #print('                   ****************')
                #print('                   **** M A K E ***')
                #print('                   ****************')
                yml_dict[i] = value.replace('make', replaceMakesBy)
            else:
                removeMakes(value)

            # print('key', key, 'value', value)


def removeIgnoredStates(stages):
    global ignored_stages

    if ignored_stages:
        for i, stage in enumerate(stages):
            if stage[0] == '.':
                stages.remove(stage)


def main():
    global python_version
    global ignored_stages
    global new_stages
    global replaceMakesBy
    global inputFile
    global outputFile

    python_version = input(
        f'Do you wanna write any special python version? ({python_version}): ') or python_version

    choice = input(
        'Do you wanna remove ignore Stages?(y/n) (default: y): ') or 'y'
    while choice not in ['y', 'n', 'Y', 'N']:
        print('Please press <Y> or <N>')
        choice = input(
            'Do you wanna remove ignore Stages?(y/n) (default: y): ')
    if choice in ['y', 'Y']:
        ignored_stages = True
    else:
        ignored_stages = False

    while s := input('Enter a new Stage or leave it blank to finish: '):
        new_stages.append(s)

    replaceMakesBy = input(
        f'Replace all "Make" by (default {replaceMakesBy}): ') or replaceMakesBy

    with open(inputFile) as fh:
        read_data = yaml.load(fh, Loader=yaml.FullLoader)

        new_data = read_data

        new_data['image'] = python_version

        # print(new_data['stages'])
        removeIgnoredStates(new_data['stages'])

        for stage in new_stages:
            new_data['stages'].append(stage)

        removeMakes(new_data)

        #  print(new_data)

        # Sort YAML data based on keys

        # print(type(new_data))

        with open(outputFile, 'w') as fw:

            sorted_data = yaml.dump(new_data, fw)

        # Print YAML data after sorting

        # yaml.save_load(sorted_data)

        print(f' Done! check out the file named {outputFile}')


if __name__ == '__main__':
    try:
        main()
    except:
        import sys
        import subprocess
        # implement pip as a subprocess:
        subprocess.check_call([sys.executable, '-r', 'pip', 'install',
                               'requirements.txt'])
