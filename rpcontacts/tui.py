from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Button, Label, DataTable, Static
from textual.containers import Grid, Vertical, Horizontal
from textual.screen import Screen

from rpcontacts.questionDialog import QuestionDialog

class ContactsApp(App):
    CSS_PATH = "rpcontacts.tcss"
    BINDINGS = [
        ("m", "toggle_dark", "Toggle dark mode"),
        ("a", "add", "Add"),
        ("d", "delete", "Delete"),
        ("c", "clear_all", "Clear All"),
        ("q", "request_quit", "Quit")
    ]

    def compose(self):
        yield Header()
        contacts_list = DataTable(classes="contacts-list")
        contacts_list.focus()
        contacts_list.add_columns("Name", "Phone", "E-mail")
        contacts_list.cursor_type = "row"
        contacts_list.zebra_stripes = True
        add_button = Button("Add", variant="success", id="add")
        add_button.focus()
        buttons_panel = Vertical(
            add_button,
            Button("Delete", variant="warning", id="delete"),
            Static(classes="separator"),
            Button("Clear All", variant="error", id="clear"),
            classes="buttons-panel"
        )
        yield Horizontal(contacts_list, buttons_panel)
        yield Footer()

    def on_mount(self):
        self.title = "RP Contacts"
        self.sub_title = "A Contacts Book App with Textual & Python"

    def action_toggle_dark(self):
        self.dark = not self.dark

    def action_request_quit(self):
        def check_answer(accepted):
            if accepted:
                self.exit()

        self.push_screen(QuestionDialog("Do you want to quit?"), check_answer)


