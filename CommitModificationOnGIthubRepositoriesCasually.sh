#!/usr/bin/env bash

# every time after i modified some files in the following repositories,
# execute this bash script will be OK!
# In this way, the auto_commit.sh file doesn't need duplicates any more actually!

tensorflow_project_path="/Users/zhaomingxing/PycharmProjects/test_tensor"
java_demo_path="/Users/zhaomingxing/IdeaProjects/hello_world/src/package_1"
python_demo_and_tool_path="/Users/zhaomingxing/PycharmProjects/python_demo_and_tool"
leetcode_path="/Users/zhaomingxing/Desktop/zmx/leetcode/leetcode_duplicate"
handbook_path="/Users/zhaomingxing/Desktop/zmx/Interesting-Github-Repositories/PythonDataScienceHandbook"

cd $tensorflow_project_path
bash auto_commit.sh

cd $java_demo_path
bash auto_commit.sh

cd $python_demo_and_tool_path
bash auto_commit.sh

cd $leetcode_path
bash auto_commit.sh

cd $handbook_path
bash auto_commit.sh



