import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from main import Ui_MainWindow
import instaloader
from instaloader import Profile


L = instaloader.Instaloader()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    
        self.ui.pushButton_4.clicked.connect(self.install_last)
        self.ui.pushButton_3.clicked.connect(self.install_all)
        self.ui.browse.clicked.connect(self.browsefiles)

    def browsefiles(self):
        fname=QFileDialog.getOpenFileName(self, 'Open file', 'D:\codefirst.io\PyQt5 tutorials\Browse Files', 'Images (*.png)')
        self.ui.filename.setText(fname[0])

    def install_last(self):
        profile_url = self.ui.lineEdit_2.text().strip()  
        username = profile_url.rstrip("/").split("/")[-1]
        profile = Profile.from_username(L.context,username)
        latest_post = next(profile.get_posts())
        L.download_post(latest_post, target = username)


    def install_all(self):
        profile_url = self.ui.lineEdit_2.text().strip()  
        username = profile_url.rstrip("/").split("/")[-1]
        profile = Profile.from_username(L.context,username)
        for post in profile.get_posts():
            L.download_post(post, target=username)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
