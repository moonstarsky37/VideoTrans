# run again.  Do not edit this file unless you know what you are doing.

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from videotrans.configure import config
from videotrans.util import tools


class Ui_deeplxform(object):
    def setupUi(self, deeplxform):
        self.has_done = False
        deeplxform.setObjectName("deeplxform")
        deeplxform.setWindowModality(QtCore.Qt.NonModal)
        deeplxform.resize(500, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(deeplxform.sizePolicy().hasHeightForWidth())
        deeplxform.setSizePolicy(sizePolicy)
        deeplxform.setMaximumSize(QtCore.QSize(500, 300))

        self.verticalLayout = QtWidgets.QVBoxLayout(deeplxform)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.formLayout_3.setObjectName("formLayout_3")
        
        
        self.label = QtWidgets.QLabel(deeplxform)
        self.label.setMinimumSize(QtCore.QSize(100, 35))
        self.label.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.deeplx_address = QtWidgets.QLineEdit(deeplxform)
        self.deeplx_address.setMinimumSize(QtCore.QSize(320, 35))
        self.deeplx_address.setObjectName("deeplx_address")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.deeplx_address)
        
        self.label2 = QtWidgets.QLabel(deeplxform)
        self.label2.setMinimumSize(QtCore.QSize(100, 35))
        self.label2.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label2.setObjectName("label2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label2)
        self.deeplx_key = QtWidgets.QLineEdit(deeplxform)
        self.deeplx_key.setMinimumSize(QtCore.QSize(320, 35))
        self.deeplx_key.setObjectName("deeplx_key")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.deeplx_key)
        
        
        self.verticalLayout.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.formLayout_3)
        
        self.set_deeplx = QtWidgets.QPushButton(deeplxform)
        self.set_deeplx.setMinimumSize(QtCore.QSize(0, 35))
        self.set_deeplx.setObjectName("set_deeplx")

        self.test = QtWidgets.QPushButton(deeplxform)
        self.test.setObjectName("test")

        help_btn = QtWidgets.QPushButton()
        help_btn.setMinimumSize(QtCore.QSize(0, 35))
        help_btn.setStyleSheet("background-color: rgba(255, 255, 255,0)")
        help_btn.setObjectName("help_btn")
        help_btn.setCursor(Qt.PointingHandCursor)
        help_btn.setText("查看填写教程" if config.defaulelang == 'zh' else "Fill out the tutorial")
        help_btn.clicked.connect(lambda: tools.open_url(url='https://pyvideotrans.com/deeplx'))

        h1=QtWidgets.QHBoxLayout()
        h1.addWidget(self.set_deeplx)
        h1.addWidget(self.test)
        h1.addWidget(help_btn)

        self.verticalLayout.addLayout(h1)


        self.retranslateUi(deeplxform)
        QtCore.QMetaObject.connectSlotsByName(deeplxform)

    def retranslateUi(self, deeplxform):
        deeplxform.setWindowTitle("DeepLx")
        self.label.setText("DeepLX_API")
        self.label2.setText("Token/Key")
        self.deeplx_key.setPlaceholderText('填写key或密钥，不存在为空即可' if config.defaulelang == 'zh' else 'Input your deeplx key ')
        self.deeplx_address.setPlaceholderText(
            '在此填写你部署的DeepLx地址' if config.defaulelang == 'zh' else 'Input your deeplx api url')
        self.set_deeplx.setText('保存' if config.defaulelang == 'zh' else "Save")
        self.test.setText('测试' if config.defaulelang == 'zh' else "Test")
