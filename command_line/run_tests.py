# LIBTBX_SET_DISPATCHER_NAME phenix.cryo_fit.run_tests
# LIBTBX_PRE_DISPATCHER_INCLUDE_SH PHENIX_GUI_ENVIRONMENT=1
# LIBTBX_PRE_DISPATCHER_INCLUDE_SH export PHENIX_GUI_ENVIRONMENT

import glob, iotbx.pdb.hierarchy, os, subprocess, sys, time
from libtbx import phil
import libtbx.phil.command_line
from libtbx.utils import Sorry
from subprocess import check_output
import libtbx.load_env
import shutil

cryo_fit_repository_dir = libtbx.env.dist_path("cryo_fit")

if (__name__ == "__main__") :

    # added by Nigel so that this test runs in a clear path
    #print "os.listdir(os.getcwd()):",os.listdir(os.getcwd())
    #print "len(os.listdir(os.getcwd())):",len(os.listdir(os.getcwd()))
    assert len(os.listdir(os.getcwd()))==0, 'run in an empty directory'
    
    # Locate phenix.cryo_fit.run_tests executable
    print "This phenix.cryo_fit.run_tests executable comes from ", cryo_fit_repository_dir
    
    splited = cryo_fit_repository_dir.split("/")
    regression_path = ''
    for i in range(len(splited)-1):
      regression_path = regression_path + splited[i] + "/"


    ############# test 1, simple biomolecule all steps ###############
    regression_path_1 = os.path.join(regression_path, 'phenix_regression/cryo_fit/emd_8249')
    print "regression_path_1:", regression_path_1
    os.chdir(regression_path_1)
    
    command_string = "python tst.py" % locals()
    libtbx.easy_run.call(command=command_string)
  
    
    ############# test 2, tutorial GTPase_activation_center, each steps ###############
    regression_path_2 = os.path.join(regression_path, 'phenix_regression/cryo_fit/GTPase_activation_center')
    print "regression_path_2:", regression_path_2
    os.chdir(regression_path_2)
    
    for i in range (1,9):
        command_string = "python tst_step_" + str(i) + ".py"
        print "command_string:", command_string
        libtbx.easy_run.call(command=command_string)
        
    command_string = "python tst_step_final.py"
    print "command_string:", command_string
    libtbx.easy_run.call(command=command_string)
  
  
    ##########  don't run this test 3, tutorial_GTPase_activation_center for all steps, since it takes 2 minutes #####
    ########## tutorial_GTPase_activation_center for each steps run individually anyway ##########
    '''
    pdb_file_name = 'GTPase_activation_center_tutorial.pdb'
    map_file_name = 'GTPase_activation_center_tutorial.map'
  
    # added by Nigel? temporarily disabled since on Doonam's macbook pro can't run this
    
    #shutil.copyfile(os.path.join(cryo_fit_repository_dir,
    #                             'tutorial_input_files',
    #                             pdb_file_name), pdb_file_name)
    #shutil.copyfile(os.path.join(cryo_fit_repository_dir,
    #                             'tutorial_input_files',
    #                             sit_file_name), sit_file_name)
  
    pdb_file_name_w_path = os.path.join(cryo_fit_repository_dir,
                                 'tutorial_input_files',
                                 pdb_file_name)
  
    map_file_name_w_path = os.path.join(cryo_fit_repository_dir,
                                 'tutorial_input_files',
                                 map_file_name)
  
    #command_string = "phenix.cryo_fit %(pdb_file_name)s %(map_file_name)s" % locals()
    command_string = "phenix.cryo_fit %(pdb_file_name_w_path)s %(map_file_name_w_path)s devel=True" % locals()
  
    print "command that will be executed: ", command_string
    print "(for your information) this run_tests took 2 minutes on Doonam's macbook pro"
    print '\n ~> %s\n' % command_string
  
  
    # as of 06/28/2018, below printout on the screen didn't print on Doonam's mac screen
    # so temporarily disabled
    
    # rc = libtbx.easy_run.go(command=command_string)
    # print '*'*80
    # for line in rc.stdout_lines:
    #   print line
    # 
    # print '*'*80
    # print rc.stderr_lines
  
    # temporarily use this instead
    libtbx.easy_run.call(command=command_string)
    '''
    