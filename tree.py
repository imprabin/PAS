# def setupUi(self, Window):
#     Window.setObjectName("Window")
#     Window.resize(800, 600)
#     self.centralwidget = QtWidgets.QWidget(Window)
#     self.centralwidget.setObjectName("centralwidget")
#     self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
#     self.verticalLayout_2.setContentsMargins(-1, 4, -1, 4)
#     self.verticalLayout_2.setObjectName("verticalLayout_2")
#     self.webView = QtWebKitWidgets.QWebView(self.centralwidget)
#     self.webView.setUrl(QtCore.QUrl("http://qt.nokia.com/"))
#     self.webView.setObjectName("webView")
#     self.verticalLayout_2.addWidget(self.webView)
#     Window.setCentralWidget(self.centralwidget)
#     self.menubar = QtWidgets.QMenuBar(Window)
#     self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
#     self.menubar.setObjectName("menubar")
#     Window.setMenuBar(self.menubar)
#     self.statusbar = QtWidgets.QStatusBar(Window)
#     self.statusbar.setObjectName("statusbar")
#     Window.setStatusBar(self.statusbar)
#     self.dockWidget = QtWidgets.QDockWidget(Window)
#     self.dockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
#     self.dockWidget.setObjectName("dockWidget")
#     self.dockWidgetContents = QtWidgets.QWidget()
#     self.dockWidgetContents.setObjectName("dockWidgetContents")
#     self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
#     self.verticalLayout.setContentsMargins(4, 4, 4, 4)
#     self.verticalLayout.setObjectName("verticalLayout")
#     self.treeWidget = QtWidgets.QTreeWidget(self.dockWidgetContents)
#     self.treeWidget.setObjectName("treeWidget")
#     self.treeWidget.headerItem().setText(0, "1")
#     self.treeWidget.header().setVisible(False)
#     self.verticalLayout.addWidget(self.treeWidget)
#     self.dockWidget.setWidget(self.dockWidgetContents)
#     Window.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
#
#     self.retranslateUi(Window)
#     QtCore.QMetaObject.connectSlotsByName(Window)

if __name__ == "__main__()":

    app = QApplication(sys.argv)
    tree = QTreeWidget()
    headerItem = QTreeWidgetItem()
    item = QTreeWidgetItem()

    for i in range(3):
        parent = QTreeWidgetItem(tree)
        parent.setText(0, "Parent {}".format(i))
        parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
        for x in range(5):
            child = QTreeWidgetItem(parent)
            child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
            child.setText(0, "Child {}".format(x))
            child.setCheckState(0, Qt.Unchecked)
    tree.show()
    sys.exit(app.exec_())

