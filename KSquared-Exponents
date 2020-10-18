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
                font_size: 30
                size_hint_y: None
                height: 100
                padding: 10, 10
                text: "Exponents Step By Step Solver"
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                height: self.minimum_height 
                
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 30
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 100
                    padding: 10, 10
                    on_release:
                        entry.text = ""
                        list_of_steps.clear_widgets()

                Button:
                    id: steps
                    text: "Clear Steps"   
                    font_size: 30
                    size_hint_y: None
                    height: 100
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets()

                        
            TextInput:
                id: entry
                text: entry.text
                multiline: False
                font_size: 30
                size_hint_y: None
                height: 75
                padding: 10
                
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: 75
                padding: 5,5      

                Button:
                    text: "^"   
                    font_size: 30
                    on_release:
                        Exponents_steps.carrot(entry)
                        entry.focus = True
    
                Button:
                    text: "-"   
                    font_size: 30
                    on_release:
                        Exponents_steps.minus_sign(entry)
                        entry.focus = True       
                            
                Button:
                    text: "Clear Entry"   
                    font_size: 30
                    padding: 10, 10
                    on_release:
                        entry.text = ""

                Button:
                    text: "Backspace"   
                    font_size: 30
                    background_color: 1, 0 , 0 , 1
                    on_release:
                        Exponents_steps.backspace(entry)
                        entry.focus = True                       
    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: 75
                padding: 5,5    
                
                Button:
                    text: "0"   
                    font_size: 30
                    on_release:
                        Exponents_steps.zero(entry)
                        entry.focus = True

                Button:
                    text: "1"   
                    font_size: 30
                    on_release:
                        Exponents_steps.one(entry)
                        entry.focus = True
                        
                Button:
                    text: "2"   
                    font_size: 30
                    on_release:
                        Exponents_steps.two(entry)
                        entry.focus = True
              
                Button:
                    text: "3"   
                    font_size: 30
                    on_release:
                        Exponents_steps.three(entry)
                        entry.focus = True
                        
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: 75
                padding: 5,5     
                
                Button:
                    text: "4"   
                    font_size: 30
                    on_release:
                        Exponents_steps.four(entry)
                        entry.focus = True

                Button:
                    text: "5"   
                    font_size: 30
                    on_release:
                        Exponents_steps.five(entry)
                        entry.focus = True
                        
                Button:
                    text: "6"   
                    font_size: 30
                    on_release:
                        Exponents_steps.six(entry)
                        entry.focus = True
              
                Button:
                    text: "7"   
                    font_size: 30
                    on_release:
                        Exponents_steps.seven(entry)
                        entry.focus = True
 

            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: 75
                padding: 5,5    
                
                Button:
                    text: "8"   
                    font_size: 30
                    on_release:
                        Exponents_steps.eight(entry)
                        entry.focus = True
                        
                Button:
                    text: "9"   
                    font_size: 30
                    on_release:
                        Exponents_steps.nine(entry)
                        entry.focus = True
                        
                Button:
                    text: "."   
                    font_size: 30
                    on_release:
                        Exponents_steps.period(entry)
                        entry.focus = True
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                height: self.minimum_height 
                
                Button:
                    id: steps
                    text: "Show Steps"   
                    font_size: 30
                    size_hint_y: None
                    background_color: 0, 1 , 0 , 1
                    height: 100
                    padding: 10, 10
                    on_release:
                        Exponents_steps.steps(entry.text)    
                        
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                  
                    

""")

class Exponents_steps(Screen):
    def carrot(self, entry):
        index_of_cursor = entry.cursor_index()
        print("entry",entry.text)
        print("index_of_cursor at index : ",index_of_cursor)
        print("left", entry.text[:index_of_cursor])
        entry.text = entry.text[:index_of_cursor] + "^" + entry.text[index_of_cursor:]
        print("manip",entry.text)    
        print()        
        entry.cursor = index_of_cursor + 1, True  
        
    def minus_sign(self, entry):
        index_of_cursor = entry.cursor_index()
        print("entry",entry.text)
        print("index_of_cursor at index : ",index_of_cursor)
        print("left", entry.text[:index_of_cursor])
        entry.text = entry.text[:index_of_cursor] + "-" + entry.text[index_of_cursor:]
        print("manip",entry.text)    
        print()        
        entry.cursor = index_of_cursor + 1, True  
        
    def zero(self, entry):
        index_of_cursor = entry.cursor_index()
        print("entry",entry.text)
        print("index_of_cursor at index : ",index_of_cursor)
        print("left", entry.text[:index_of_cursor])
        entry.text = entry.text[:index_of_cursor] + "0" + entry.text[index_of_cursor:]
        print("manip",entry.text)        
        print()        
        entry.cursor = index_of_cursor + 1, True    
        
    def one(self, entry):
        index_of_cursor = entry.cursor_index()
        print("entry",entry.text)
        print("index_of_cursor at index : ",index_of_cursor)
        print("left", entry.text[:index_of_cursor])
        entry.text = entry.text[:index_of_cursor] + "1" + entry.text[index_of_cursor:]
        print("manip",entry.text)        
        print()        
        entry.cursor = index_of_cursor + 1, True         
        
    def two(self, entry):
        index_of_cursor = entry.cursor_index()
        print("entry",entry.text)
        print("index_of_cursor at index : ",index_of_cursor)
        print("left", entry.text[:index_of_cursor])
        entry.text = entry.text[:index_of_cursor] + "2" + entry.text[index_of_cursor:]
        print("manip",entry.text)        
        print()        
        entry.cursor = index_of_cursor + 1, True             
        
    def three(self, entry):
        index_of_cursor = entry.cursor_index()
        print("entry",entry.text)
        print("index_of_cursor at index : ",index_of_cursor)
        print("left", entry.text[:index_of_cursor])
        entry.text = entry.text[:index_of_cursor] + "3" + entry.text[index_of_cursor:]
        print("manip",entry.text)        
        print()        
        entry.cursor = index_of_cursor + 1, True
    
    def four(self, entry):
        index_of_cursor = entry.cursor_index()
        print("entry",entry.text)
        print("index_of_cursor at index : ",index_of_cursor)
        print("left", entry.text[:index_of_cursor])
        entry.text = entry.text[:index_of_cursor] + "4" + entry.text[index_of_cursor:]
        print("manip",entry.text)        
        print()        
        entry.cursor = index_of_cursor + 1, True 
    
    def five(self, entry):
        index_of_cursor = entry.cursor_index()
        print("entry",entry.text)
        print("index_of_cursor at index : ",index_of_cursor)
        print("left", entry.text[:index_of_cursor])
        entry.text = entry.text[:index_of_cursor] + "5" + entry.text[index_of_cursor:]
        print("manip",entry.text)        
        print()        
        entry.cursor = index_of_cursor + 1, True
    
    def six(self, entry):
        index_of_cursor = entry.cursor_index()
        print("entry",entry.text)
        print("index_of_cursor at index : ",index_of_cursor)
        print("left", entry.text[:index_of_cursor])
        entry.text = entry.text[:index_of_cursor] + "6" + entry.text[index_of_cursor:]
        print("manip",entry.text)        
        print()        
        entry.cursor = index_of_cursor + 1, True  
    
    def seven(self, entry):
        index_of_cursor = entry.cursor_index()
        print("entry",entry.text)
        print("index_of_cursor at index : ",index_of_cursor)
        print("left", entry.text[:index_of_cursor])
        entry.text = entry.text[:index_of_cursor] + "7" + entry.text[index_of_cursor:]
        print("manip",entry.text)        
        print()        
        entry.cursor = index_of_cursor + 1, True    
    
    def eight(self, entry):
        index_of_cursor = entry.cursor_index()
        print("entry",entry.text)
        print("index_of_cursor at index : ",index_of_cursor)
        print("left", entry.text[:index_of_cursor])
        entry.text = entry.text[:index_of_cursor] + "8" + entry.text[index_of_cursor:]
        print("manip",entry.text)        
        print()        
        entry.cursor = index_of_cursor + 1, True        
    
    def nine(self, entry):
        index_of_cursor = entry.cursor_index()
        print("entry",entry.text)
        print("index_of_cursor at index : ",index_of_cursor)
        print("left", entry.text[:index_of_cursor])
        entry.text = entry.text[:index_of_cursor] + "9" + entry.text[index_of_cursor:]
        print("manip",entry.text)        
        print()        
        entry.cursor = index_of_cursor + 1, True    
        
    def period(self, entry):
        index_of_cursor = entry.cursor_index()
        print("entry",entry.text)
        print("index_of_cursor at index : ",index_of_cursor)
        print("left", entry.text[:index_of_cursor])
        entry.text = entry.text[:index_of_cursor] + "." + entry.text[index_of_cursor:]
        print("manip",entry.text)        
        print()        
        entry.cursor = index_of_cursor + 1, True 
        
    def backspace(self,entry):
        index_of_cursor = entry.cursor_index()
        print("index_of_cursor at index : ",index_of_cursor)
        print("left", entry.text[:index_of_cursor])
        entry.text = entry.text[:index_of_cursor-1] + entry.text[index_of_cursor:]
        print("entry", entry.text)
        entry.cursor = index_of_cursor - 1, True 

    layouts = []
    def steps(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        self.ids.list_of_steps.add_widget(Label(text="Expression entered : " + entry.replace(" ",""), font_size = 30, size_hint_y= None, height=100))
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
                    self.ids.list_of_steps.add_widget(Label(text="Expanded form of : " + display, font_size = 30, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text=expand, font_size = 30, size_hint_y= None, height=100))
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
                self.ids.list_of_steps.add_widget(Label(text="Exponents step of : " + display + " = " + solved +  "  :  ", font_size = 30, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text=entry, font_size = 30, size_hint_y= None, height=100))
                self.layouts.append(layout)
            i = i + 1
            
            entry = str(format(float(entry),",")).replace("(","").replace(")","")
            print()
            print("entry formatted :    ",entry)
            self.ids.list_of_steps.add_widget(Label(text="Final Answer : " + entry, font_size = 30, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 30, size_hint_y= None, height=100))
            self.layouts.append(layout)    
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 30, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 30, size_hint_y= None, height=100))
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
