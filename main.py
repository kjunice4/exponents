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
                size_hint_y: None
                height: 400
                text: "Visit KSquared,LLC"
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc')
            Button:
                font_size: 75
                size_hint_y: None
                height: 400
                text: "Other apps from KSquared,LLC"
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc/subscribe')   
                
            Button:
                font_size: 75
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
                    input_filter: lambda text, from_undo: text[:2 - len(Base_entry.text)]           
            
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
                    input_filter: lambda text, from_undo: text[:2 - len(Power_entry.text)]           
            
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
            print("entry split: ",entry)
            print()
            
            base = entry_list[0]
            print("base",base)
            
            power = entry_list[1]
            print("power",power)
            
            self.ids.list_of_steps.add_widget(Label(text= base + " is multiplied " + power + " time(s)", font_size = 60, size_hint_y= None, height=100))
            
            i = 0
            product = base
            power_ = power
            while i < int(power_):
                length = product + (" * " + base) * (int(power) - 1)
                self.ids.list_of_steps.add_widget(Label(text= length ,font_size = 60, size_hint_y= None, height=100))
                power = int(power) - 1
                product = "{:,}".format(int(product.replace(",","")) * int(base))
                i = i + 1
            
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
    
