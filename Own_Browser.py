import sys  #imports system
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.browser = QWebEngineView()  #function from where the browser will work
        self.browser.setUrl(QUrl('http://google.com'))  #Building URL
        self.setCentralWidget(self.browser)   #Contains features
        self.showMaximized()

        #Navigation Bar
        navigation_bar = QToolBar()
        self.addToolBar(navigation_bar)

        #making buttons on browser
        back_button = QAction('Back', self)  #defining action
        back_button.triggered.connect(self.browser.back)  #connects to browser and apply the button
        navigation_bar.addAction(back_button)  #setting the position of back button to navigation bar

        forward_button = QAction('Forward', self)
        forward_button.triggered.connect(self.browser.forward)
        navigation_bar.addAction(forward_button)

        reload_button = QAction('Reload', self)
        reload_button.triggered.connect(self.browser.reload)
        navigation_bar.addAction(reload_button)

        home_button = QAction('Home', self)
        home_button.triggered.connect(self.navigate_home)
        navigation_bar.addAction(home_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navigation_bar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):  #setting home page
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):  #to search on browser
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):  #updating url when webisites are switched.
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)  #indicates we are making own browser and opens in new window
QApplication.setApplicationName('KHOJ')  #Giving Name
main = Window()  #making object
app.exec_()  #exe file for app. In app QApplication is present