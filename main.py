from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen


#PEMDAS STEPS
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Exponents_steps"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 30
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared Exponent Step By Step Solver"
            on_release:
                app.root.current = "Exponents_steps"
                root.manager.transition.direction = "left" 

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
                text: "Exponents Step By Step Solver"
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    id: steps
                    text: "Clear Steps"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets()

                Button:
                    text: "Clear Entry"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 1, 0 , 0 , 1
                    on_release:
                        Exponent_entry.text = ""
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
                    Exponent_entry.text = ""
                    Base_entry.text = ""
                    list_of_steps.clear_widgets()              
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
        
                Label:
                    font_size: 30
                    size_hint_y: None
                    height: 200
                    font_size: 75
                    padding: 10, 10
                    text: "Base:"
                                                        
                TextInput:
                    id: Base_entry
                    text: Base_entry.text
                    multiline: False
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10
                                
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5        
        
                Label:
                    font_size: 30
                    size_hint_y: None
                    height: 200
                    font_size: 75
                    padding: 10, 10
                    text: "Power:"
                                                    
                TextInput:
                    id: Power_entry
                    text: Power_entry.text
                    multiline: False
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10              
                
            Button:
                id: steps
                text: "Show Steps"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    Exponents_steps.steps(Base_entry.text + "^" + Power_entry.text)    
                        
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                  
                    

""")

class Exponents_steps(Screen):
    
    layouts = []
    def steps(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        self.ids.list_of_steps.add_widget(Label(text="Expression entered : " + entry.replace(" ",""), font_size = 75, size_hint_y= None, height=100))
        self.layouts.append(layout)
        try:
            i = 0
            while i < entry.count("^"):
                entry = list(entry.split("^"))
                print("entry ;", entry)
                display = str(entry[0]) + "^" + str(entry[1])
                print()
                print("display : ",display)
                if entry[1].count(".") == 0 and entry[1].count("-") == 0:
                    mult_signs =  " * " + entry[0]
                    print()
                    print("mult_signs",mult_signs)
                    times = int(entry[1]) - 1
                    print()
                    print("times",times)
                    expand = entry[0] + mult_signs * times
                    print()
                    print("expand",expand)
                    self.ids.list_of_steps.add_widget(Label(text="Expanded form of : " + display, font_size = 75, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text=expand, font_size = 75, size_hint_y= None, height=100))
                    self.layouts.append(layout)

                solved = str(float(entry[0]) ** float(entry[1]))
                print()
                print("solved :", solved)
                entry[0] = str(float(entry[0]) ** float(entry[1]))
                print()
                print("entry[0] :",entry[0])
                if entry[1] != "":
                    entry.pop(1)
                print()
                print("entry list:", entry)
                print()
                entry = str(entry).replace("[","").replace("]","").replace("'","").replace(","," ^")
                print("entry string :",entry)
                print()
                self.ids.list_of_steps.add_widget(Label(text="Exponents step of : " + display + " = " + solved +  "  :  ", font_size = 75, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text=entry, font_size = 75, size_hint_y= None, height=100))
                self.layouts.append(layout)
            i = i + 1
            
            entry = str(format(float(entry),",")).replace("(","").replace(")","")
            print()
            print("entry formatted :    ",entry)
            self.ids.list_of_steps.add_widget(Label(text="Final Answer : " + entry, font_size = 75, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 75, size_hint_y= None, height=100))
            self.layouts.append(layout)    
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 75, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 75, size_hint_y= None, height=100))
            self.layouts.append(layout)  


class Homepage(Screen):
    pass            
           
           
sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Exponents_steps(name="Exponents_steps"))      
sm.current = "Homepage"   


class Exponents(App):
    def build(app):
        return sm

if __name__ == '__main__':
    Exponents().run()
    

