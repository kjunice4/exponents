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
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Tap anywhere to continue"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"        

        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 100
            text: "KSquared-Mathematics"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 100
            text: "Exponents Calculator"
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
                height: 200
                padding: 10, 10
                text: "Visit KSquared-Mathematics"
                on_release:
                    import webbrowser
                    webbrowser.open('https://www.ksquaredmathematics.com/subscribe') 
                    
            Button:
                font_size: 75
                background_color: 1, 0, 1, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new?"
                on_release:
                    app.root.current = "updates"
                    root.manager.transition.direction = "left"
                    
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Share KSquared-Mathematics"
                    
            Image:
                source: 'KSquared_QR.png'
                size_hint_y: None
                height: 1000
                width: 1000
""")

#Updates
Builder.load_string("""
<updates>
    id:updates
    name:"updates"
    
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
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new at KSquared-Mathematics?"
            
            Button:
                id: steps
                text: "Menu"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 0 , 1 , 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Menu"
                    root.manager.transition.direction = "right" 
                    
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Exponents Calculator v0.1"
                
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "No new updates as of 1/26/2022"
            
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
                text: "Exponents Calculator"
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 

                Button:
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        Power_entry.text = ""
                        Base_entry.text = ""
                        list_of_steps.clear_widgets()       
                        
            Label:
                font_size: '20sp'
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
                    font_size: '35sp'
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
                    font_size: '35sp'
                    size_hint_y: None
                    height: 200
                    padding: 10              
                    input_filter: lambda text, from_undo: text[:2 - len(Power_entry.text)]           
            
            Button:
                id: steps
                text: "Calculate"   
                font_size: '20sp'
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
            
    layouts = []
    def steps(self,entry):
        print()
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        try:
            print("entry",entry)
            display = entry.replace("$","^")
            entry_list = entry.split("$")
            print("display :" + display)
            self.ids.list_of_steps.add_widget(Label(text="Expression entered : " + display, font_size = '20sp', size_hint_y= None, height=100))
            Answer = str(eval(str(display).replace("^","**")))
            Answer = "{:,}".format(float(Answer.replace(",","")))
            print("Answer",Answer)
            self.ids.list_of_steps.add_widget(Label(text="Answer: " + '[color=33CAFF]' + Answer + '[/color]', markup=True, font_size = '20sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            entry = entry_list
            print("entry split: ",entry)
            print()
            
            base = entry_list[0]
            print("base",base)
            
            power = entry_list[1]
            print("power",power)
            
            if power.find("-") < 0:
                self.ids.list_of_steps.add_widget(Label(text="Proof of work:", font_size = '20sp', size_hint_y= None, height=100))
                
                i = 0
                product = base
                power_ = power
                while i < float(power_):
                    length = '[color=33CAFF]' + product + '[/color]' + " * " + base
                    print("length",length)
                    if int(power) > 1:
                        self.ids.list_of_steps.add_widget(Label(text= length ,font_size = '20sp', markup=True, size_hint_y= None, height=100))
                    else:
                        self.ids.list_of_steps.add_widget(Label(text= '[color=33CAFF]' + product + '[/color]', markup=True, font_size = '20sp', size_hint_y= None, height=100))
                    power = int(power) - 1
                    print("power",power)
                    product = "{:,}".format(float(product.replace(",","")) * float(base))
                    print("product",product)
                    i = i + 1
            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '20sp', size_hint_y= None, height=100))
            self.layouts.append(layout)  
                
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass

class updates(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))     
sm.add_widget(Exponents_steps(name="Exponents_steps"))     
sm.add_widget(updates(name="updates"))
sm.current = "Homepage"   

class Exponents(App):
    def __init__(self, **kwargs):
        super(Exponents, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
    
    def _key_handler(self, instance, key, *args):
        print("key:",key)
        if key == 27:
            sm.current = sm.current
            return True
    
    
    def build(app):
        return sm

if __name__ == '__main__':
    Exponents().run()
    

