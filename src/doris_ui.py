# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doris.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1186, 971)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lb_frames = QtWidgets.QLabel(self.centralwidget)
        self.lb_frames.setObjectName("lb_frames")
        self.horizontalLayout_5.addWidget(self.lb_frames)
        self.pb_1st_frame = QtWidgets.QPushButton(self.centralwidget)
        self.pb_1st_frame.setObjectName("pb_1st_frame")
        self.horizontalLayout_5.addWidget(self.pb_1st_frame)
        self.pb_next_frame = QtWidgets.QPushButton(self.centralwidget)
        self.pb_next_frame.setObjectName("pb_next_frame")
        self.horizontalLayout_5.addWidget(self.pb_next_frame)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.le_goto_frame = QtWidgets.QLineEdit(self.centralwidget)
        self.le_goto_frame.setObjectName("le_goto_frame")
        self.horizontalLayout_5.addWidget(self.le_goto_frame)
        self.pb_goto_frame = QtWidgets.QPushButton(self.centralwidget)
        self.pb_goto_frame.setObjectName("pb_goto_frame")
        self.horizontalLayout_5.addWidget(self.pb_goto_frame)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.sb_frame_offset = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_frame_offset.setMinimum(1)
        self.sb_frame_offset.setMaximum(10000)
        self.sb_frame_offset.setSingleStep(10)
        self.sb_frame_offset.setProperty("value", 1)
        self.sb_frame_offset.setObjectName("sb_frame_offset")
        self.horizontalLayout_5.addWidget(self.sb_frame_offset)
        self.pb_backward = QtWidgets.QPushButton(self.centralwidget)
        self.pb_backward.setObjectName("pb_backward")
        self.horizontalLayout_5.addWidget(self.pb_backward)
        self.pb_forward = QtWidgets.QPushButton(self.centralwidget)
        self.pb_forward.setObjectName("pb_forward")
        self.horizontalLayout_5.addWidget(self.pb_forward)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.cb_threshold_method = QtWidgets.QComboBox(self.centralwidget)
        self.cb_threshold_method.setObjectName("cb_threshold_method")
        self.cb_threshold_method.addItem("")
        self.cb_threshold_method.addItem("")
        self.cb_threshold_method.addItem("")
        self.horizontalLayout.addWidget(self.cb_threshold_method)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.sb_blur = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_blur.setProperty("value", 2)
        self.sb_blur.setObjectName("sb_blur")
        self.horizontalLayout_10.addWidget(self.sb_blur)
        self.cb_invert = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_invert.setObjectName("cb_invert")
        self.horizontalLayout_10.addWidget(self.cb_invert)
        self.cb_background = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_background.setEnabled(False)
        self.cb_background.setObjectName("cb_background")
        self.horizontalLayout_10.addWidget(self.cb_background)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lb_threshold = QtWidgets.QLabel(self.centralwidget)
        self.lb_threshold.setObjectName("lb_threshold")
        self.horizontalLayout_4.addWidget(self.lb_threshold)
        self.sb_threshold = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_threshold.setMaximum(255)
        self.sb_threshold.setObjectName("sb_threshold")
        self.horizontalLayout_4.addWidget(self.sb_threshold)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_4.addWidget(self.label_16)
        self.sb_block_size = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_block_size.setProperty("value", 10)
        self.sb_block_size.setObjectName("sb_block_size")
        self.horizontalLayout_4.addWidget(self.sb_block_size)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_4.addWidget(self.label_17)
        self.sb_offset = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_offset.setProperty("value", 10)
        self.sb_offset.setObjectName("sb_offset")
        self.horizontalLayout_4.addWidget(self.sb_offset)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pb_define_arena = QtWidgets.QPushButton(self.centralwidget)
        self.pb_define_arena.setObjectName("pb_define_arena")
        self.horizontalLayout_16.addWidget(self.pb_define_arena)
        self.pb_clear_arena = QtWidgets.QPushButton(self.centralwidget)
        self.pb_clear_arena.setEnabled(False)
        self.pb_clear_arena.setObjectName("pb_clear_arena")
        self.horizontalLayout_16.addWidget(self.pb_clear_arena)
        self.le_arena = QtWidgets.QLineEdit(self.centralwidget)
        self.le_arena.setReadOnly(True)
        self.le_arena.setObjectName("le_arena")
        self.horizontalLayout_16.addWidget(self.le_arena)
        self.verticalLayout_9.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.sbMin = QtWidgets.QSpinBox(self.centralwidget)
        self.sbMin.setMaximum(100000)
        self.sbMin.setSingleStep(10)
        self.sbMin.setProperty("value", 0)
        self.sbMin.setObjectName("sbMin")
        self.horizontalLayout_2.addWidget(self.sbMin)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.sbMax = QtWidgets.QSpinBox(self.centralwidget)
        self.sbMax.setMaximum(100000)
        self.sbMax.setSingleStep(10)
        self.sbMax.setProperty("value", 0)
        self.sbMax.setObjectName("sbMax")
        self.horizontalLayout_3.addWidget(self.sbMax)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setEnabled(False)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.sb_largest_number = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_largest_number.setEnabled(False)
        self.sb_largest_number.setMaximum(999)
        self.sb_largest_number.setObjectName("sb_largest_number")
        self.horizontalLayout_7.addWidget(self.sb_largest_number)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_17.addWidget(self.label_13)
        self.sb_max_extension = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_max_extension.setMaximum(9999999)
        self.sb_max_extension.setSingleStep(100)
        self.sb_max_extension.setObjectName("sb_max_extension")
        self.horizontalLayout_17.addWidget(self.sb_max_extension)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_17)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_9.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_all = QtWidgets.QLabel(self.centralwidget)
        self.lb_all.setObjectName("lb_all")
        self.verticalLayout.addWidget(self.lb_all)
        self.te_all_objects = QtWidgets.QTextEdit(self.centralwidget)
        self.te_all_objects.setObjectName("te_all_objects")
        self.verticalLayout.addWidget(self.te_all_objects)
        self.pb_show_all_objects = QtWidgets.QPushButton(self.centralwidget)
        self.pb_show_all_objects.setObjectName("pb_show_all_objects")
        self.verticalLayout.addWidget(self.pb_show_all_objects)
        self.horizontalLayout_9.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lb_filtered = QtWidgets.QLabel(self.centralwidget)
        self.lb_filtered.setObjectName("lb_filtered")
        self.verticalLayout_2.addWidget(self.lb_filtered)
        self.te_filtered_objects = QtWidgets.QTextEdit(self.centralwidget)
        self.te_filtered_objects.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.te_filtered_objects.setObjectName("te_filtered_objects")
        self.verticalLayout_2.addWidget(self.te_filtered_objects)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lb_filtered_2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_filtered_2.setObjectName("lb_filtered_2")
        self.verticalLayout_4.addWidget(self.lb_filtered_2)
        self.te_tracked_objects = QtWidgets.QTextEdit(self.centralwidget)
        self.te_tracked_objects.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.te_tracked_objects.setObjectName("te_tracked_objects")
        self.verticalLayout_4.addWidget(self.te_tracked_objects)
        self.horizontalLayout_9.addLayout(self.verticalLayout_4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout_11.addWidget(self.label)
        self.le_coordinates_center = QtWidgets.QLineEdit(self.tab)
        self.le_coordinates_center.setReadOnly(True)
        self.le_coordinates_center.setObjectName("le_coordinates_center")
        self.horizontalLayout_11.addWidget(self.le_coordinates_center)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.cb_record_xy = QtWidgets.QCheckBox(self.tab)
        self.cb_record_xy.setObjectName("cb_record_xy")
        self.verticalLayout_5.addWidget(self.cb_record_xy)
        self.te_xy = QtWidgets.QTextEdit(self.tab)
        self.te_xy.setObjectName("te_xy")
        self.verticalLayout_5.addWidget(self.te_xy)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pb_reset_xy = QtWidgets.QPushButton(self.tab)
        self.pb_reset_xy.setObjectName("pb_reset_xy")
        self.horizontalLayout_12.addWidget(self.pb_reset_xy)
        self.pb_save_xy = QtWidgets.QPushButton(self.tab)
        self.pb_save_xy.setObjectName("pb_save_xy")
        self.horizontalLayout_12.addWidget(self.pb_save_xy)
        self.pb_plot_path = QtWidgets.QPushButton(self.tab)
        self.pb_plot_path.setObjectName("pb_plot_path")
        self.horizontalLayout_12.addWidget(self.pb_plot_path)
        self.pb_plot_xy_density = QtWidgets.QPushButton(self.tab)
        self.pb_plot_xy_density.setObjectName("pb_plot_xy_density")
        self.horizontalLayout_12.addWidget(self.pb_plot_xy_density)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.cb_record_number_objects = QtWidgets.QCheckBox(self.tab_2)
        self.cb_record_number_objects.setObjectName("cb_record_number_objects")
        self.verticalLayout_7.addWidget(self.cb_record_number_objects)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.lw_area_definition = QtWidgets.QListWidget(self.tab_2)
        self.lw_area_definition.setObjectName("lw_area_definition")
        self.verticalLayout_7.addWidget(self.lw_area_definition)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pb_add_area = QtWidgets.QPushButton(self.tab_2)
        self.pb_add_area.setObjectName("pb_add_area")
        self.horizontalLayout_13.addWidget(self.pb_add_area)
        self.pb_remove_area = QtWidgets.QPushButton(self.tab_2)
        self.pb_remove_area.setObjectName("pb_remove_area")
        self.horizontalLayout_13.addWidget(self.pb_remove_area)
        self.pb_open_areas = QtWidgets.QPushButton(self.tab_2)
        self.pb_open_areas.setObjectName("pb_open_areas")
        self.horizontalLayout_13.addWidget(self.pb_open_areas)
        self.pb_save_areas = QtWidgets.QPushButton(self.tab_2)
        self.pb_save_areas.setObjectName("pb_save_areas")
        self.horizontalLayout_13.addWidget(self.pb_save_areas)
        self.pb_active_areas = QtWidgets.QPushButton(self.tab_2)
        self.pb_active_areas.setObjectName("pb_active_areas")
        self.horizontalLayout_13.addWidget(self.pb_active_areas)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_15.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.te_number_objects = QtWidgets.QTextEdit(self.tab_2)
        self.te_number_objects.setObjectName("te_number_objects")
        self.verticalLayout_8.addWidget(self.te_number_objects)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pb_reset_areas = QtWidgets.QPushButton(self.tab_2)
        self.pb_reset_areas.setObjectName("pb_reset_areas")
        self.horizontalLayout_14.addWidget(self.pb_reset_areas)
        self.pb_save_objects_number = QtWidgets.QPushButton(self.tab_2)
        self.pb_save_objects_number.setObjectName("pb_save_objects_number")
        self.horizontalLayout_14.addWidget(self.pb_save_objects_number)
        self.verticalLayout_8.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15.addLayout(self.verticalLayout_8)
        self.verticalLayout_10.addLayout(self.horizontalLayout_15)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_9.addWidget(self.tabWidget)
        self.cb_display_analysis = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_display_analysis.setChecked(True)
        self.cb_display_analysis.setObjectName("cb_display_analysis")
        self.verticalLayout_9.addWidget(self.cb_display_analysis)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pb_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pb_stop.setObjectName("pb_stop")
        self.horizontalLayout_6.addWidget(self.pb_stop)
        self.pbGo = QtWidgets.QPushButton(self.centralwidget)
        self.pbGo.setObjectName("pbGo")
        self.horizontalLayout_6.addWidget(self.pbGo)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1186, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuFrame_viewer_scale = QtWidgets.QMenu(self.menuSettings)
        self.menuFrame_viewer_scale.setObjectName("menuFrame_viewer_scale")
        self.menuTreatment_viewer_scale = QtWidgets.QMenu(self.menuSettings)
        self.menuTreatment_viewer_scale.setObjectName("menuTreatment_viewer_scale")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_video = QtWidgets.QAction(MainWindow)
        self.actionOpen_video.setObjectName("actionOpen_video")
        self.actionBackground = QtWidgets.QAction(MainWindow)
        self.actionBackground.setObjectName("actionBackground")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionFrame_width = QtWidgets.QAction(MainWindow)
        self.actionFrame_width.setObjectName("actionFrame_width")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLoad_directory_of_images = QtWidgets.QAction(MainWindow)
        self.actionLoad_directory_of_images.setObjectName("actionLoad_directory_of_images")
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action1_2 = QtWidgets.QAction(MainWindow)
        self.action1_2.setObjectName("action1_2")
        self.action1_4 = QtWidgets.QAction(MainWindow)
        self.action1_4.setObjectName("action1_4")
        self.action_treated_1 = QtWidgets.QAction(MainWindow)
        self.action_treated_1.setObjectName("action_treated_1")
        self.action_treated_1_2 = QtWidgets.QAction(MainWindow)
        self.action_treated_1_2.setObjectName("action_treated_1_2")
        self.action_treated_1_4 = QtWidgets.QAction(MainWindow)
        self.action_treated_1_4.setObjectName("action_treated_1_4")
        self.actionSave_project = QtWidgets.QAction(MainWindow)
        self.actionSave_project.setObjectName("actionSave_project")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action_treated_2 = QtWidgets.QAction(MainWindow)
        self.action_treated_2.setObjectName("action_treated_2")
        self.actionOpen_project = QtWidgets.QAction(MainWindow)
        self.actionOpen_project.setObjectName("actionOpen_project")
        self.actionDraw_reference = QtWidgets.QAction(MainWindow)
        self.actionDraw_reference.setObjectName("actionDraw_reference")
        self.actionDefine_coordinate_center = QtWidgets.QAction(MainWindow)
        self.actionDefine_coordinate_center.setCheckable(False)
        self.actionDefine_coordinate_center.setObjectName("actionDefine_coordinate_center")
        self.actionSelect_objects_to_track = QtWidgets.QAction(MainWindow)
        self.actionSelect_objects_to_track.setCheckable(False)
        self.actionSelect_objects_to_track.setObjectName("actionSelect_objects_to_track")
        self.menuFile.addAction(self.actionOpen_video)
        self.menuFile.addAction(self.actionLoad_directory_of_images)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_project)
        self.menuFile.addAction(self.actionSave_project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuFrame_viewer_scale.addAction(self.action2)
        self.menuFrame_viewer_scale.addAction(self.action1)
        self.menuFrame_viewer_scale.addAction(self.action1_2)
        self.menuFrame_viewer_scale.addAction(self.action1_4)
        self.menuTreatment_viewer_scale.addAction(self.action_treated_2)
        self.menuTreatment_viewer_scale.addAction(self.action_treated_1)
        self.menuTreatment_viewer_scale.addAction(self.action_treated_1_2)
        self.menuTreatment_viewer_scale.addAction(self.action_treated_1_4)
        self.menuSettings.addAction(self.menuFrame_viewer_scale.menuAction())
        self.menuSettings.addAction(self.menuTreatment_viewer_scale.menuAction())
        self.menuSettings.addAction(self.actionDraw_reference)
        self.menuSettings.addAction(self.actionDefine_coordinate_center)
        self.menuSettings.addAction(self.actionSelect_objects_to_track)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lb_frames.setText(_translate("MainWindow", "Number of frames: "))
        self.pb_1st_frame.setText(_translate("MainWindow", "Go to 1st frame"))
        self.pb_next_frame.setText(_translate("MainWindow", "next frame"))
        self.label_11.setText(_translate("MainWindow", "frame number"))
        self.le_goto_frame.setText(_translate("MainWindow", "1"))
        self.pb_goto_frame.setText(_translate("MainWindow", "Go to"))
        self.label_10.setText(_translate("MainWindow", "Step"))
        self.pb_backward.setText(_translate("MainWindow", "go backward"))
        self.pb_forward.setText(_translate("MainWindow", "go forward"))
        self.label_9.setText(_translate("MainWindow", "Image processing"))
        self.label_14.setText(_translate("MainWindow", "Threshold method"))
        self.cb_threshold_method.setItemText(0, _translate("MainWindow", "Adaptive (mean)"))
        self.cb_threshold_method.setItemText(1, _translate("MainWindow", "Adaptive (Gaussian)"))
        self.cb_threshold_method.setItemText(2, _translate("MainWindow", "Simple"))
        self.label_8.setText(_translate("MainWindow", "Blur"))
        self.cb_invert.setText(_translate("MainWindow", "Invert"))
        self.cb_background.setText(_translate("MainWindow", "Substract background"))
        self.lb_threshold.setText(_translate("MainWindow", "Simple threshold: cut-off"))
        self.label_15.setText(_translate("MainWindow", "Adaptive threshold:"))
        self.label_16.setText(_translate("MainWindow", "Block size"))
        self.label_17.setText(_translate("MainWindow", "Offset"))
        self.label_5.setText(_translate("MainWindow", "Objects"))
        self.pb_define_arena.setText(_translate("MainWindow", "Define arena"))
        self.pb_clear_arena.setText(_translate("MainWindow", "Clear arena"))
        self.label_12.setText(_translate("MainWindow", "Filters"))
        self.label_3.setText(_translate("MainWindow", "min obj size"))
        self.label_4.setText(_translate("MainWindow", "max obj size"))
        self.label_7.setText(_translate("MainWindow", "Number of largest objects"))
        self.label_13.setText(_translate("MainWindow", "Max object extension"))
        self.lb_all.setText(_translate("MainWindow", "All detected objects"))
        self.pb_show_all_objects.setText(_translate("MainWindow", "Show all objects"))
        self.lb_filtered.setText(_translate("MainWindow", "Filtered objects"))
        self.lb_filtered_2.setText(_translate("MainWindow", "Tracked objects"))
        self.label.setText(_translate("MainWindow", "Coordinates center"))
        self.cb_record_xy.setText(_translate("MainWindow", "record objects coordinates"))
        self.pb_reset_xy.setText(_translate("MainWindow", "Reset"))
        self.pb_save_xy.setText(_translate("MainWindow", "Save results"))
        self.pb_plot_path.setText(_translate("MainWindow", "Plot path"))
        self.pb_plot_xy_density.setText(_translate("MainWindow", "plot XY density"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Objects coordinates"))
        self.cb_record_number_objects.setText(_translate("MainWindow", "Record number of objects(s) in areas"))
        self.label_2.setText(_translate("MainWindow", "Areas"))
        self.pb_add_area.setText(_translate("MainWindow", "Add area"))
        self.pb_remove_area.setText(_translate("MainWindow", "Remove selected area"))
        self.pb_open_areas.setText(_translate("MainWindow", "Load areas from disk"))
        self.pb_save_areas.setText(_translate("MainWindow", "Save areas to disk"))
        self.pb_active_areas.setText(_translate("MainWindow", "Activate areas"))
        self.label_6.setText(_translate("MainWindow", "Number of object(s) in areas"))
        self.pb_reset_areas.setText(_translate("MainWindow", "Reset"))
        self.pb_save_objects_number.setText(_translate("MainWindow", "Save results"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Area"))
        self.cb_display_analysis.setText(_translate("MainWindow", "Display analysis"))
        self.pb_stop.setText(_translate("MainWindow", "Stop"))
        self.pbGo.setText(_translate("MainWindow", "Run analysis"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuFrame_viewer_scale.setTitle(_translate("MainWindow", "Frame viewer scale"))
        self.menuTreatment_viewer_scale.setTitle(_translate("MainWindow", "Treatment viewer scale"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_video.setText(_translate("MainWindow", "Open video"))
        self.actionBackground.setText(_translate("MainWindow", "background"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionFrame_width.setText(_translate("MainWindow", "Frame width"))
        self.actionAbout.setText(_translate("MainWindow", "About DORIS"))
        self.actionLoad_directory_of_images.setText(_translate("MainWindow", "Load directory of images"))
        self.action1.setText(_translate("MainWindow", "1"))
        self.action1_2.setText(_translate("MainWindow", "1/2"))
        self.action1_4.setText(_translate("MainWindow", "1/4"))
        self.action_treated_1.setText(_translate("MainWindow", "1"))
        self.action_treated_1_2.setText(_translate("MainWindow", "1/2"))
        self.action_treated_1_4.setText(_translate("MainWindow", "1/4"))
        self.actionSave_project.setText(_translate("MainWindow", "Save project"))
        self.action2.setText(_translate("MainWindow", "2"))
        self.action_treated_2.setText(_translate("MainWindow", "2"))
        self.actionOpen_project.setText(_translate("MainWindow", "Open project"))
        self.actionDraw_reference.setText(_translate("MainWindow", "Draw reference"))
        self.actionDefine_coordinate_center.setText(_translate("MainWindow", "Define coordinate center"))
        self.actionSelect_objects_to_track.setText(_translate("MainWindow", "Select objects to track"))

