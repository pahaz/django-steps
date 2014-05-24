import glob
import os
import re
import sys
import shutil

__author__ = 'pahaz'

RE_EXCLUDE_NAME_FOR_FIXES = u"^(db|media|static)"
STEP_PREFIX = u"_step_"

DIR_PATTERN = STEP_PREFIX + u"(\\d+)"
NEXT_STEP_FORMAT = STEP_PREFIX + u"{index:02}{name}"


def _error(msg):
    msg = msg.strip('\n') + '\n'
    sys.stderr.write(msg)


def last_step(re_dir_name=DIR_PATTERN):
    """
    return tuple(last_step_index, last_step_name)
    """
    re_dir_name = re.compile(re_dir_name)
    match = lambda xxx: re_dir_name.match(xxx)
    steps = [(int(match(x).group(1)), x) for x in glob.glob('*') if match(x)]
    steps = sorted(steps, key=lambda x: x[0])
    if not steps:
        raise Exception("Please init first step!")
    return steps[-1]


def next_step(name='', re_dir_name=DIR_PATTERN):
    """
    return tuple(next_step_index, next_step_name)
    """
    last_step_index, last_step_name = last_step(re_dir_name)
    name_with_prefix = "_" + name if name else ''
    next_step_index = last_step_index + 1
    next_step_name = NEXT_STEP_FORMAT.format(
        index=next_step_index, name=name_with_prefix)
    return next_step_index, next_step_name


def fix_content_in(root_dir, pattern, repl, ignore=None):
    """
    Replace pattern -> repl in content if each file.
    """
    for root, dirs, files in os.walk(root_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if ignore and ignore.match(file_name):
                continue

            try:
                with open(file_path) as f:
                    fixed_content = pattern.sub(repl, f.read())
                with open(file_path, 'w') as f:
                    f.write(fixed_content)
            except OSError as e:
                _error(u"{1} when open('{0}')".format(file_path, e))
                continue

        if ignore:
            for dir_name in dirs:
                if ignore.match(dir_name):
                    dirs.remove(dir_name)


def fix_naming_in(root_dir, pattern, repl, ignore=None):
    """
    Replace pattern -> repl in name of each file and each dir.
    """
    def _rename_all(root, names):
        for name in names[:]:
            path = os.path.join(root, name)
            if ignore and ignore.match(name):
                names.remove(name)
                continue
            try:
                new_name = pattern.sub(repl, name)
                new_path = os.path.join(root, new_name)
                os.rename(path, new_path)
                names.remove(name)
                names.append(new_name)
            except OSError as e:
                _error(u"{1} when rename('{0}')".format(path, e))
                continue

    for root, dirs, files in os.walk(root_dir):
        _rename_all(root, files)
        _rename_all(root, dirs)


def main():
    next_step_index, next_step_name = next_step()
    last_step_index, last_step_name = last_step()
    shutil.copytree(last_step_name, next_step_name)
    _find = re.compile('_project_v{0:02}_'.format(last_step_index))
    _repl = '_project_v{0:02}_'.format(next_step_index)
    _ignore = re.compile(RE_EXCLUDE_NAME_FOR_FIXES)
    fix_content_in(next_step_name, _find, _repl, _ignore)
    fix_naming_in(next_step_name, _find, _repl, _ignore)


if __name__ == "__main__":
    main()
