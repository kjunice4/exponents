from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 75
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared Exponents Calculator"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 

""")

# Menu
Builder.load_string("""
<Menu>
    id:Menu
    name:"Menu"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Menu"
            
            Button:
                text: "Exponents Calculator"   
                font_size: 75
                background_color: 0, 0 , 1 , 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Exponents_steps"
                    root.manager.transition.direction = "left" 
                    
            Button:
                font_size: 75
                background_color: 0, 0 , 0 , 1
                size_hint_y: None
                height: 400
                text: "Visit KSquared,LLC"
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc')
            Button:
                font_size: 75
                background_color: 0, 0 , 0 , 1
                size_hint_y: None
                height: 400
                text: "Other apps from KSquared,LLC"
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc/subscribe')   
                
            Button:
                font_size: 75
                background_color: 0, 0 , 0 , 1
                size_hint_y: None
                height: 400
                text: "Donate to KSquared,LLC"
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc/about-ksquared')
            
""")

#EXPONENTS STEPS
Builder.load_string("""
<Exponents_steps>
    id:Exponents_steps
    name:"Exponents_steps"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Exponents Solver"
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 

                Button:
                    text: "Clear Entry"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    on_release:
                        Power_entry.text = ""
                        Base_entry.text = ""
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        Power_entry.text = ""
                        Base_entry.text = ""
                        list_of_steps.clear_widgets()       
                        
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Base ^ Power"
                
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
        
                TextInput:
                    id: Base_entry
                    text: Base_entry.text
                    hint_text: "Base:"
                    multiline: False
                    font_size: 125
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:3 - len(Base_entry.text)]           
            
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5        
        
                TextInput:
                    id: Power_entry
                    text: Power_entry.text
                    hint_text: "Power:"
                    multiline: False
                    font_size: 125
                    size_hint_y: None
                    height: 200
                    padding: 10              
                    input_filter: lambda text, from_undo: text[:3 - len(Power_entry.text)]           
            
            Button:
                id: steps
                text: "Calculate"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    Exponents_steps.steps(Base_entry.text + "$" + Power_entry.text)    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class Exponents_steps(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Exponents_steps, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        if sm.current != "Homepage":
            sm.transition.direction = 'right'
            sm.current = "Menu"
    layouts = []
    def steps(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        print("entry",entry)
        display = entry.replace("$","^")
        entry_list = entry.split("$")
        print("display :" + display)
        self.ids.list_of_steps.add_widget(Label(text="Expression entered : " + display, font_size = 60, size_hint_y= None, height=100))
        self.layouts.append(layout)
        
        try:
            entry = entry_list
            print("entry split : ",entry)
            print()
            print("entry[0]: " + entry[0])
            print("entry[1]: " + entry[1])
            entry_one = entry[0]
            print("length entry_one ",len(entry_one))
            entry_two = entry[1]
            if entry_one.count("e") > 0 and len(entry_one) == 1:
                entry_one = "2.71828"
            elif entry_one.count("e") > 0 and len(entry_one) == 2:
                if entry_one == "ee":
                    entry_one = "2.71828*2.71828"
                elif entry_one[0] == "e":
                    entry_one = "2.71828*" + entry_one[1]
                elif entry_one[1] == "e":
                    entry_one = entry_one[0] + "*2.71828"
            elif entry_one.count("e") > 0 and len(entry_one) == 3:
                if entry_one.count("e") == 1:
                    if entry_one[0] == "e": 
                        entry_one = "2.71828*" + entry_one[1:]
                    if entry_one[1] == "e":
                        entry_one = entry_one[0] + "2.71828*" + entry_one[2]
                    if entry_one[2] == "e":
                        entry_one = entry_one[:2] + "*2.71828"
                if entry_one.count("e") == 2:    
                    if entry_one.count("ee") > 0:
                        entry_one = entry_one.replace("ee","_2.71828*2.71828_")
                        if entry_one[0] == "_":
                            entry_one = entry_one[1:]
                        elif entry_one[-1] == "_":
                            entry_one = entry_one[:-1]
                        entry_one = entry_one.replace("_","*")
                    elif entry_one[0] == "e" and entry_one[2] == "e":
                        entry_one = "2.71828*" + entry_one[1] + "*2.71828"
                if entry_one.count("e") == 3:
                    entry_one = "2.71828*2.71828*2.71828"
                
            if entry_two.count("e") > 0 and len(entry_two) == 1:
                entry_two = "2.71828"
            elif entry_two.count("e") > 0 and len(entry_two) == 2:
                if entry_two == "ee":
                    entry_two = "2.71828*2.71828"
                elif entry_two[0] == "e":
                    entry_two = "2.71828*" + entry_two[1]
                elif entry_two[1] == "e":
                    entry_two = entry_two[0] + "*2.71828"
            elif entry_two.count("e") > 0 and len(entry_two) == 3:
                if entry_two.count("e") == 1:
                    if entry_two[0] == "e": 
                        entry_two = "2.71828*" + entry_two[1:]
                    if entry_two[1] == "e":
                        entry_two = entry_two[0] + "2.71828*" + entry_two[2]
                    if entry_two[2] == "e":
                        entry_two = entry_two[:2] + "*2.71828"
                if entry_two.count("e") == 2:    
                    if entry_two.count("ee") > 0:
                        entry_two = entry_two.replace("ee","_2.71828*2.71828_")
                        if entry_two[0] == "_":
                            entry_two = entry_two[1:]
                        elif entry_two[-1] == "_":
                            entry_two = entry_two[:-1]
                        entry_two = entry_two.replace("_","*")
                    elif entry_two[0] == "e" and entry_two[2] == "e":
                        entry_two = "2.71828*" + entry_two[1] + "*2.71828"
                if entry_two.count("e") == 3:
                    entry_two = "2.71828*2.71828*2.71828"            
            print("entry_one",entry_one)   
            print("entry_two",entry_two) 
            entry_one = entry_one.replace("*^","**").replace("^*","**")
            entry_two = entry_two.replace("*^","**").replace("^*","**")
            solved = str(eval(str(entry_one).replace("^","**")) ** eval(str(entry_two).replace("^","**")))
            print()
            print("solved :", solved)
            print()
            solved = str(format(float(solved),","))
            print("solved formatted :    ",solved)
            self.ids.list_of_steps.add_widget(Label(text= display + " = " + solved , font_size = 60, size_hint_y= None, height=100))
        
        except Exception:
            try:
                self.ids.list_of_steps.add_widget(Label(text= "Out Of Range" ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
                    
            except Exception:               
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)  
                
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))     
sm.add_widget(Exponents_steps(name="Exponents_steps"))     
sm.current = "Homepage"   


class Exponents(App):
    def build(app):
        return sm

if __name__ == '__main__':
    Exponents().run()
    

