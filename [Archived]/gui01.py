# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import glob
import numpy as np
import os
import subprocess
import time

import gsyIO
import gsyINI

from PyQt5 import QtCore, QtGui, QtWidgets

CONST_EXPT_EMF = '--export-emf='
CONST_INI_FILENAME = 'gsySVG2EMF.ini'

class Ui_SVG2EMF(object):

    def setupUi(self, SVG2EMF):

        SVG2EMF.setObjectName("SVG2EMF")
        SVG2EMF.resize(470, 325)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SVG2EMF.sizePolicy().hasHeightForWidth())
        SVG2EMF.setSizePolicy(sizePolicy)
        SVG2EMF.setMinimumSize(QtCore.QSize(470, 325))
        SVG2EMF.setMaximumSize(QtCore.QSize(4000, 400))
        self.centralwidget = QtWidgets.QWidget(SVG2EMF)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gLayout_folders = QtWidgets.QGridLayout()
        self.gLayout_folders.setObjectName("gLayout_folders")
        self.btn_browse_svg = QtWidgets.QPushButton(self.centralwidget)
        self.btn_browse_svg.setObjectName("btn_browse_svg")
        self.gLayout_folders.addWidget(self.btn_browse_svg, 1, 2, 1, 1)
        self.ledt_svg_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_svg_dir.setObjectName("ledt_svg_dir")
        self.gLayout_folders.addWidget(self.ledt_svg_dir, 1, 1, 1, 1)
        self.lbl_emf_dir = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_emf_dir.setFont(font)
        self.lbl_emf_dir.setObjectName("lbl_emf_dir")
        self.gLayout_folders.addWidget(self.lbl_emf_dir, 2, 0, 1, 1)
        self.lbl_svg_dir = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_svg_dir.setFont(font)
        self.lbl_svg_dir.setObjectName("lbl_svg_dir")
        self.gLayout_folders.addWidget(self.lbl_svg_dir, 1, 0, 1, 1)
        self.ledt_emf_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_emf_dir.setObjectName("ledt_emf_dir")
        self.gLayout_folders.addWidget(self.ledt_emf_dir, 2, 1, 1, 1)
        self.btn_browse_emf = QtWidgets.QPushButton(self.centralwidget)
        self.btn_browse_emf.setObjectName("btn_browse_emf")
        self.gLayout_folders.addWidget(self.btn_browse_emf, 2, 2, 1, 1)
        self.ledt_inkscape_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.ledt_inkscape_dir.setObjectName("ledt_inkscape_dir")
        self.gLayout_folders.addWidget(self.ledt_inkscape_dir, 0, 1, 1, 1)
        self.lbl_inkscape_dir = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_inkscape_dir.setFont(font)
        self.lbl_inkscape_dir.setObjectName("lbl_inkscape_dir")
        self.gLayout_folders.addWidget(self.lbl_inkscape_dir, 0, 0, 1, 1)
        self.btn_browse_inkscape = QtWidgets.QPushButton(self.centralwidget)
        self.btn_browse_inkscape.setObjectName("btn_browse_inkscape")
        self.gLayout_folders.addWidget(self.btn_browse_inkscape, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gLayout_folders)
        self.vLayout = QtWidgets.QVBoxLayout()
        self.vLayout.setObjectName("vLayout")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.vLayout.addWidget(self.checkBox)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.vLayout.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.vLayout)
        self.hLayout_btn = QtWidgets.QHBoxLayout()
        self.hLayout_btn.setObjectName("hLayout_btn")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setStyleSheet("font: 75 9pt \"Helvetica\";")
        self.btn_exit.setObjectName("btn_exit")
        self.hLayout_btn.addWidget(self.btn_exit)
        self.btn_open_svg = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_svg.setStyleSheet("font: 75 9pt \"Helvetica\";")
        self.btn_open_svg.setObjectName("btn_open_svg")
        self.hLayout_btn.addWidget(self.btn_open_svg)
        self.btn_open_emf = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_emf.setStyleSheet("font: 75 9pt \"Helvetica\";")
        self.btn_open_emf.setObjectName("btn_open_emf")
        self.hLayout_btn.addWidget(self.btn_open_emf)
        self.btn_go = QtWidgets.QPushButton(self.centralwidget)
        self.btn_go.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 9pt \"Helvetica\";")
        self.btn_go.setObjectName("btn_go")
        self.hLayout_btn.addWidget(self.btn_go)
        self.verticalLayout.addLayout(self.hLayout_btn)
        self.lbl_copyright = QtWidgets.QLabel(self.centralwidget)
        self.lbl_copyright.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        self.lbl_copyright.setFont(font)
        self.lbl_copyright.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.lbl_copyright.setObjectName("lbl_copyright")
        self.verticalLayout.addWidget(self.lbl_copyright)
        SVG2EMF.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SVG2EMF)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 470, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        SVG2EMF.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SVG2EMF)
        self.statusbar.setObjectName("statusbar")
        SVG2EMF.setStatusBar(self.statusbar)
        self.act_file_exit = QtWidgets.QAction(SVG2EMF)
        self.act_file_exit.setObjectName("act_file_exit")
        self.act_help_doct = QtWidgets.QAction(SVG2EMF)
        self.act_help_doct.setObjectName("act_help_doct")
        self.act_help_about = QtWidgets.QAction(SVG2EMF)
        self.act_help_about.setObjectName("act_help_about")
        self.act_file_go = QtWidgets.QAction(SVG2EMF)
        self.act_file_go.setObjectName("act_file_go")
        self.menuFile.addAction(self.act_file_go)
        self.menuFile.addAction(self.act_file_exit)
        self.menuHelp.addAction(self.act_help_doct)
        self.menuHelp.addAction(self.act_help_about)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(SVG2EMF)

        # attributes, directories
        self.str_inkscape_dir = None
        self.str_svg_dir = None
        self.str_emf_dir = None

        # connects
        self.act_file_exit.triggered['bool'].connect(SVG2EMF.close)
        
        self.btn_browse_inkscape.clicked.connect(self.get_inkscape_dir)
        self.btn_browse_svg.clicked.connect(self.get_svg_dir)
        self.btn_browse_emf.clicked.connect(self.get_emf_dir)

        self.btn_exit.clicked['bool'].connect(SVG2EMF.close)

        self.btn_open_svg.clicked.connect(self.open_svg_folder)
        self.btn_open_emf.clicked.connect(self.open_emf_folder)
        
        self.btn_go.clicked.connect(self.convert)

        # read saved setting
        self.read_setting()

        QtCore.QMetaObject.connectSlotsByName(SVG2EMF)

        SVG2EMF.setTabOrder(self.ledt_inkscape_dir, self.btn_browse_inkscape)
        SVG2EMF.setTabOrder(self.btn_browse_inkscape, self.ledt_svg_dir)
        SVG2EMF.setTabOrder(self.ledt_svg_dir, self.btn_browse_svg)
        SVG2EMF.setTabOrder(self.btn_browse_svg, self.ledt_emf_dir)
        SVG2EMF.setTabOrder(self.ledt_emf_dir, self.btn_browse_emf)
        SVG2EMF.setTabOrder(self.btn_browse_emf, self.btn_go)
        SVG2EMF.setTabOrder(self.btn_go, self.btn_open_emf)
        SVG2EMF.setTabOrder(self.btn_open_emf, self.btn_open_svg)
        SVG2EMF.setTabOrder(self.btn_open_svg, self.btn_exit)

    def retranslateUi(self, SVG2EMF):
        _translate = QtCore.QCoreApplication.translate
        SVG2EMF.setWindowTitle(_translate("SVG2EMF", "SVG2EMF © Dr. GAO, Siyu"))
        self.btn_browse_svg.setText(_translate("SVG2EMF", "Browse"))
        self.lbl_emf_dir.setText(_translate("SVG2EMF", "<html><head/><body><p>EMF folder</p></body></html>"))
        self.lbl_svg_dir.setText(_translate("SVG2EMF", "<html><head/><body><p>SVG folder</p></body></html>"))
        self.btn_browse_emf.setText(_translate("SVG2EMF", "Browse"))
        self.lbl_inkscape_dir.setText(_translate("SVG2EMF", "<html><head/><body><p>Inkscape folder</p></body></html>"))
        self.btn_browse_inkscape.setText(_translate("SVG2EMF", "Browse"))
        self.checkBox.setText(_translate("SVG2EMF", "Open EMF folder on end"))
        self.btn_exit.setText(_translate("SVG2EMF", "Exit"))
        self.btn_open_svg.setText(_translate("SVG2EMF", "Open SVG folder"))
        self.btn_open_emf.setText(_translate("SVG2EMF", "Open EMF folder"))
        self.btn_go.setText(_translate("SVG2EMF", "Go"))
        self.lbl_copyright.setText(_translate("SVG2EMF", "© Dr.GAO, Siyu; 2018\n"
"siyu.gao@outlook.com"))
        self.menuFile.setTitle(_translate("SVG2EMF", "File"))
        self.menuHelp.setTitle(_translate("SVG2EMF", "Help"))
        self.act_file_exit.setText(_translate("SVG2EMF", "Exit"))
        self.act_help_doct.setText(_translate("SVG2EMF", "Documentation"))
        self.act_help_about.setText(_translate("SVG2EMF", "About"))
        self.act_file_go.setText(_translate("SVG2EMF", "Go"))
        self.act_file_go.setShortcut(_translate("SVG2EMF", "Ctrl+G"))

    def check_inkscape_bin(self, str_inkscape_dir):
        """
        This function checks whether there is at least one file starts 
        with "inkscape" in the directory (non-recursive).

        Parameter
        ----------
        str_inkscape_dir : str
            The intended Inkscape installation directory.

        Return
        -------
        bool :
            Returns True if at least one file under the directory starts 
            with "inkscape". Returns False if no file starts with 
            "inkscape".
        
        Example
        --------
        .. code:: python
        
            bool_temp = self.check_inkscape_bin(str_temp)
        """

        # form search pattern
        str_pattern = str_inkscape_dir + os.sep + 'inkscape*'

        # search, if not, would return a empty list
        list_temp = glob.glob(str_pattern, recursive=False)

        # if list empty, return False (empty list is False by itself)
        if not list_temp:

            return False

        # if list not empty, return True
        else:

            return True

    def get_inkscape_dir(self):
        """
        This function pompts a folder select dialogue to allow the user
        to select the Inkscape installation folder.

        This function then sets the text of the Inkscape QLineEdit object.

        If the folder is found, the text would be set to the path of the 
        folder.

        If the folder is not found, the text would be set to empty string.

        Parameter
        ----------
        self
        
        Return
        -------
        None 
        
        Example
        --------
        .. code:: python
        
            self.btn_browse_inkscape.clicked.connect(self.get_inkscape_dir)
        """

        # prompt folder select dialogue
        str_temp = gsyIO.get_dir(str_title='Select the Inkscape installation folder')

        # see if the Inkscape binary is in the selected folder
        bool_temp = self.check_inkscape_bin(str_temp)

        # if exists, set path to line edit
        if bool_temp == True:

            self.ledt_inkscape_dir.setText(str_temp)

        # if not exists, prompt error message
        else:

            gsyIO.prompt_msg(str_title='Inkscape binary not found',
                             str_msg='Inkscape binary not found',
                             str_type='err')

            self.ledt_inkscape_dir.setText('')

    def get_svg_dir(self):
        """
        This function pompts a folder select dialogue to allow the user
        to select the folder that contains the SVG files to be converted.

        This function then sets the text of the SVG QLineEdit object.

        If the folder is found, the text would be set to the path of the 
        folder.

        If the folder is not found, the text would be set to empty string.

        Parameter
        ----------
        self
        
        Return
        -------
        None 
        
        Example
        --------
        .. code:: python
        
            self.btn_browse_svg.clicked.connect(self.get_svg_dir)
        """

        # prompt folder select dialogue
        str_temp = gsyIO.get_dir(str_title='Select the folder for SVG files')

        # set text to line edit
        self.ledt_svg_dir.setText(str_temp)

    def get_emf_dir(self):
        """
        This function pompts a folder select dialogue to allow the user
        to select the folder for the exported EMF files.

        This function then sets the text of the EMF QLineEdit object.

        If the folder is found, the text would be set to the path of the 
        folder.

        If the folder is not found, the text would be set to empty string.

        Parameter
        ----------
        self
        
        Return
        -------
        None 
        
        Example
        --------
        .. code:: python
        
            self.btn_browse_emf.clicked.connect(self.get_emf_dir)
        """
        
        # prompt folder select dialogue
        str_temp = gsyIO.get_dir(str_title='Select the folder to export EMF files')

        # set text to line edit
        self.ledt_emf_dir.setText(str_temp)

    def open_emf_folder(self):
        """
        This function opens the folder for EMF files in explorer.

        If the folder is not found, a error message would be prompted.

        Parameter
        ----------
        self
        
        Return
        -------
        None 
        
        Example
        --------
        .. code:: python
        
            self.open_emf_folder()
        """

        # get folder path from the line edit
        str_folder_path = self.ledt_emf_dir.text()

        # if folder not found, prompt error message
        if os.path.isdir(str_folder_path) == False:

            gsyIO.prompt_msg(str_title='Folder not found',
                             str_msg='EMF folder not found',
                             str_type='err')

        # if folder found, try to open it in explorer
        else:

            gsyIO.open_folder(str_folder_path)

    def open_svg_folder(self):
        """
        This function opens the folder for SVG files in explorer.

        If the folder is not found, a error message would be prompted.

        Parameter
        ----------
        self
        
        Return
        -------
        None 
        
        Example
        --------
        .. code:: python
        
            self.open_svg_folder()
        """

        # get folder path from the line edit
        str_folder_path = self.ledt_svg_dir.text()

        # if folder not found, prompt error message
        if os.path.isdir(str_folder_path) == False:

            gsyIO.prompt_msg(str_title='Folder not found',
                             str_msg='SVG folder not found',
                             str_type='err')

        # if folder found, try to open it in explorer
        else:

            gsyIO.open_folder(str_folder_path)

    def update_dir(self):
        """
        This function transfers the text in the QLineEdit objects to 
        the attributes.

        Parameter
        ----------
        self
        
        Return
        -------
        None 
        
        Example
        --------
        .. code:: python
        
            self.update_dir()
        """
        
        # transfer the text in the QLineEdits to attributes
        self.str_inkscape_dir   = self.ledt_inkscape_dir.text()
        self.str_svg_dir        = self.ledt_svg_dir.text()
        self.str_emf_dir        = self.ledt_emf_dir.text()

    def check_dir_exist(self):
        """
        This function checks if all selected directories exist.

        This function would call "update_dir" first before checking.

        Parameter
        ----------
        self
        
        Return
        -------
        bool
            Returns True if all directories exist. 
            Returns False if not all exist (if one or more not exists).
        
        Example
        --------
        .. code:: python
        
            self.check_dir_exist()
        """

        # transfer the text in the QLineEdits to attributes
        self.update_dir()

        # get the directories exist states
        bool_inkscape_dir = os.path.isdir(self.str_inkscape_dir)

        bool_svg_dir = os.path.isdir(self.str_svg_dir)

        bool_emf_dir = os.path.isdir(self.str_emf_dir)

        # check if the directories all exist
        list_temp = [bool_inkscape_dir, bool_svg_dir, bool_emf_dir]

        bool_dir_exist = all(x == True for x in list_temp)

        return bool_dir_exist

    def search_svg(self):
        """
        This function searchs for the SVG files in the 
        selected directory (recursively).

        This function would call "update_dir" first before searching.

        Parameter
        ----------
        self
        
        Return
        -------
        bool or list
            Returns False if the selected directory not found.
            Returns a list of SVG file paths if the directory is found.

            Note that, an empty list if a boolean False.
        
        Example
        --------
        .. code:: python
        
            list_svg_file_path = self.search_svg()
        """

        self.update_dir()

        # check if the SVG folder exists or not
        # if not exist, return False
        if os.path.isdir(self.str_svg_dir) == False:

            return False
        
        # if the folder exist, return the search list
        # not that an empty list is a boolean False
        else:

            str_pattern = self.str_svg_dir + os.sep + '**' + os.sep + '*.svg'

            list_svg_file = glob.glob(str_pattern, recursive=True)

            return list_svg_file

    def convert(self):
        """
        This function converts the SVG files found to EMF files.

        The filenames of the SVG files would be kept.

        Overwirte files with the same filenames without notice.

        Conversion is achieved via Inkscape. 
        
        The command is in the form of:

        .. code::

            inkscape foo.svg --export-emf=bar.emf

        Parameter
        ----------
        self
        
        Return
        -------
        bool
            Returns True if conversion successful.
            Returns False if conversion unsuccessful or on exception.
        
        Example
        --------
        .. code:: python
        
            self.btn_go.clicked.connect(self.convert)
        """

        print(gsyIO.date_time_now() + 'Converting...')

        # progress bar control
        int_count = 0

        dbl_progress = 0

        self.progressBar.setValue(dbl_progress)

        # check if all folders exist
        bool_dir_exist = self.check_dir_exist()

        try:

            # if not all folders exist, prompt error message and return False
            if bool_dir_exist == False:

                gsyIO.prompt_msg(str_title='Folder not found',
                                str_msg='At least one folder not found',
                                str_type='err')

                print(gsyIO.date_time_now() + 'At least one folder not found')
                print(gsyIO.date_time_now() + 'Conversion failed')

                return False

            else:
                
                # first part of the shell command
                str_inkscape = '"' + self.str_inkscape_dir + os.sep + 'inkscape' + '"'

                # search for SVG files
                list_svg_file_path = self.search_svg()

                # if the list is empty
                if not list_svg_file_path:

                    gsyIO.prompt_msg(str_title='SVG not found',
                                    str_msg='No SVG file found',
                                    str_type='err')

                    print(gsyIO.date_time_now() + 'No SVG file found')
                    print(gsyIO.date_time_now() + 'Conversion failed')

                    return False

                else:
                    
                    # save user settings
                    self.save_setting()

                    # get the total number of SVG files in the list
                    int_svg_file_count = len(list_svg_file_path)

                    # For-Loop through the SVG files and convert to EMF
                    for item in list_svg_file_path:

                        str_svg_file_path = item

                        # reverse find first path separator
                        index = str_svg_file_path.rfind(os.sep)

                        # get the filename (only) of the SVG file
                        str_svg_filename = str_svg_file_path[(index + 1):]

                        # find the "." of the SVG extension
                        index = str_svg_filename.rfind('.')

                        # replace the "svg" for "emf"
                        str_emf_filename = str_svg_filename[:(index + 1)] + 'emf'

                        # form the full path for the EMF file
                        str_emf_file_path = os.path.join(self.str_emf_dir, str_emf_filename)

                        # form the shell command
                        str_cmd = (str_inkscape + ' ' 
                                + '"' + str_svg_file_path + '"' + ' ' 
                                + '"' + CONST_EXPT_EMF + str_emf_file_path + '"')

                        # run the shell command, timeout is 10 minutes
                        obj = subprocess.run(str_cmd, shell=True, timeout=600)

                        # progress bar control
                        int_count += 1

                        dbl_progress = float(int_count) / float(int_svg_file_count) * 100.0

                        str_info = ('Converting ' + str(int_count) + ' of ' + str(int_svg_file_count)
                                    + ', ' + '{:.2f}'.format(dbl_progress) + r'%')

                        print(str_info)

                        self.progressBar.setValue(dbl_progress)

                    # open EMF folder on end
                    if self.checkBox.isChecked() == True:

                        self.open_emf_folder()

                    else:

                        pass

                    print(gsyIO.date_time_now() + 'Conversion complete')

                    return True

        except:

            print(gsyIO.date_time_now() + 'Conversion failed')

            return False

    def save_setting(self):
        """
        This function saves the user setting to an INI file.

        Parameter
        ----------
        self
        
        Return
        -------
        None
        
        Example
        --------
        .. code:: python
        
            self.save_setting()
        """

        print(gsyIO.date_time_now() + 'Saving settings...')

        # form INI file content
        str_setting = '[User settings]\n'

        str_setting += 'ledt_inkscape_dir=' + self.ledt_inkscape_dir.text() + '\n'

        str_setting += 'ledt_svg_dir=' + self.ledt_svg_dir.text() + '\n'

        str_setting += 'ledt_emf_dir=' + self.ledt_emf_dir.text() + '\n'

        str_setting += 'checkBox=' + str(self.checkBox.isChecked())

        # form INI file path
        str_ini_file_path = os.path.join(os.getcwd(), CONST_INI_FILENAME)

        # save INI file
        gsyINI.write_ini(str_ini_file_path, str_setting)

    def read_setting(self):
        """
        This function reads the user setting from an INI file and
        then assigns them to the objects.

        Parameter
        ----------
        self
        
        Return
        -------
        None
        
        Example
        --------
        .. code:: python
        
            self.read_setting()
        """
        
        # get INI file path
        str_ini_file_path = os.path.join(os.getcwd(), CONST_INI_FILENAME)

        # read INI file
        bool_ini_exist, str_setting = gsyINI.read_ini(str_ini_file_path)

        # if INI file not found, return False
        if bool_ini_exist == False:

            print(gsyIO.date_time_now() + 'Read user setting failed.')

            return False

        else:

            pass

        try:

            # get rid of the line breaks
            str_setting = [item.strip('\n') for item in str_setting]

            str_setting = [item.strip('\r') for item in str_setting]

            # list for QLineEdit
            list_widget = [self.ledt_inkscape_dir, self.ledt_svg_dir,
                           self.ledt_emf_dir]

            # assign values
            for item in str_setting:
                
                # keep the left of "="
                index = item.find('=')

                str_temp_setting = item[:index]

                # assign the checkbox
                if str_temp_setting == 'checkBox':

                    str_temp = item[(index + 1):]

                    if str_temp == 'True':

                        self.checkBox.setChecked(True)

                    else:

                        self.checkBox.setChecked(False)

                # assign the QLineEdit
                for j in list_widget:

                    if str_temp_setting == j.objectName():

                        j.setText(item[(index + 1):])

                        # if found, remove from list
                        list_widget.pop(list_widget.index(j))

                        break

                    else:

                        pass

            print(gsyIO.date_time_now() + 'Read user setting complete')

            return True

        except:

            print(gsyIO.date_time_now() + 'Read user setting failed.')

            return False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join('./image', 'convert.png')))

    SVG2EMF = QtWidgets.QMainWindow()
    ui = Ui_SVG2EMF()
    ui.setupUi(SVG2EMF)
    SVG2EMF.show()
    sys.exit(app.exec_())

