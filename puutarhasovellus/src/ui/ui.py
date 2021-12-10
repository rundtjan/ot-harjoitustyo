from ui.login_view import LoginView
from ui.registration_view import RegistrationView
from ui.main_view import MainView
from ui.add_plantation_view import AddPlantationView
from ui.edit_plantation_view import EditPlantationView
from ui.edit_planting_date_view import EditPlantingDateView
from ui.edit_yield_date_view import EditYieldDateView
from ui.choose_year_view import ChooseYearView

class UI:
    '''Master class for all UI:s
    '''
    def __init__(self, root):
        '''Constructor.

        Args:
            root: the tkinter-root-object

        Also initializes a _current-variable that keeps track of and manipulizes which window the UI is showing.

        '''

        self._root = root
        self._current = None

    def start(self):
        '''Function that starts the UI by showing the login-window
        '''
        self._show_login()

    def _hide_current(self):
        '''Function that hides any view that might be active
        '''
        if self._current:
            self._current.destroy()

        self._current = None

    def _show_login(self):
        '''Function that shows the login window
        '''
        self._hide_current()
        self._current = LoginView(self._root, self._show_registration, self._show_mainview, self._show_adminview)
        self._current.pack()

    def _show_registration(self):
        '''Function that shows the registration window
        '''
        self._hide_current()
        self._current = RegistrationView(self._root, self._show_login)
        self._current.pack()

    def _show_mainview(self):
        '''Function that shows the mainview window
        '''
        self._hide_current()
        self._current = MainView(self._root, self._show_login, self._add_plantation, self._show_edit_plantation, self._show_adminview, self._show_choose_year)
        self._current.pack()

    def _show_adminview(self):
        '''Function that shows the admin window
        '''
        pass

    def _add_plantation(self):
        self._hide_current()
        self._current = AddPlantationView(self._root, self._show_mainview)
        self._current.pack()

    def _show_edit_plantation(self, plant_id):
        self._hide_current()
        self._current= EditPlantationView(self._root, self._show_mainview, self._edit_planting_date, self._edit_yield_date, plant_id)
        self._current.pack()

    def _edit_planting_date(self, plant_id):
        self._hide_current()
        self._current = EditPlantingDateView(self._root, self._show_edit_plantation, plant_id)
        self._current.pack()

    def _edit_yield_date(self, plant_id):
        self._hide_current()
        self._current = EditYieldDateView(self._root, self._show_edit_plantation, plant_id)
        self._current.pack()
    
    def _show_choose_year(self):
        self._hide_current()
        self._current = ChooseYearView(self._root, self._show_mainview)
        self._current.pack()
