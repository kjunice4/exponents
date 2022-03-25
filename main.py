#Algebra Bundle

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import numpy as np
import sympy as sym
from colorama import Back, Style 
from sympy import Limit, Symbol, S, diff, integrate
import math

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
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Tap anywhere to continue"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
        
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared-math,LLC © : Algebra Bundle"
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
                
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Algebra"
                
            Button:
                text: "Domain and Range"
                font_size: 75
                background_color: 0, 0 , 1 , 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Domain_and_Range"
                    root.manager.transition.direction = "left"    
                    
            Button:
                text: "Exponents Calculator"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 0, 1, 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Exponents_steps"
                    root.manager.transition.direction = "left"    
            
            Button:
                text: "FOIL Method"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 0, 1, 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "FOIL"
                    root.manager.transition.direction = "left"
            
            Button:
                text: "PEMDAS"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 0, 1, 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "PEMDAS"
                    root.manager.transition.direction = "left"       
            
            Button:
                text: "Quadratic Calculator"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 0, 1, 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Quadratic_Formula_Solver"
                    root.manager.transition.direction = "left"
                    
""")

#Domain_and_Range Calculator 
Builder.load_string("""
<Domain_and_Range>
    id:Domain_and_Range
    name:"Domain_and_Range"
    
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
                text: "Domain and Range"
                    
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
                    font_size: 75
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
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        y.text = ""
                        domain.text = ""
                        list_of_steps.clear_widgets()            
                    
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "f(x) = ax + b"       
                                                        
            TextInput:
                id: y
                text: y.text
                multiline: False
                hint_text: "f(x) ="
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10
                    
            TextInput:
                id: domain
                text: domain.text
                multiline: False
                hint_text:"Domain = min,max,sequence"
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10  
                
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
                    Domain_and_Range.steps(y.text + "&" + domain.text)  
                
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                  
                    
""")

class Domain_and_Range(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Domain_and_Range, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            print("Its working ESC = 27 LENGTH")
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        print("Length is almost working")        
        if sm.current != "Homepage":
            print("Its working List")
            sm.transition.direction = 'right'
            sm.current = sm.previous()
            
    layouts = []
    def steps(self,entry):
        print()
        print("~~~~~~~~~~~~~~~~")
        print("entry ",entry)
        entry.replace(" ","")
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            print()
            amp = entry.find("&")
            y = entry[:amp]
            print("y:",y)
            
            self.ids.list_of_steps.add_widget(Label(text= "y = " + y.replace(" ","").replace("y=","").replace("+"," + ").replace("-"," - ") ,font_size = 60, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            domain = entry[amp+1:]
            print("domain",domain)
            
            domain_comma = domain.find(",")
            comma_count = domain.count(",")
            
            print("domain_comma",domain_comma)
            
            if comma_count == 0 and y.count("x") > 0:
                y = y.replace("x","*" + str(domain)).replace("+*","+").replace("-*","-").replace("/*","/").replace("(*","(").replace("(*","(").replace("sqrt","math.sqrt").replace("pi","math.pi").replace("^","**").replace("sin","math.sin").replace("cos","math.cos").replace("tan","math.tan").replace("csc","mpmath.csc").replace("sec","mpmath.sec").replace("cot","mpmath.cot").replace("log","math.log").replace("e","math.e").replace("smath.ec","mp.sec").replace("math.smath.secc","mp.sec").replace("math.math","math").replace("mp.mp","mp")
                print("y = ",y)
                if y[0] == "*":
                    y = y.replace("*","")
                y = y.replace("^","**")
                y = str(eval(y))
                
                self.ids.list_of_steps.add_widget(Label(text= "Domain | Range" ,font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "x | y" ,font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(domain) + " | " + str(y) ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
            elif comma_count == 1 and y.count("x") > 0:
                
                empty_domain = []
                for x in range(int(domain[:domain_comma]), int(domain[domain_comma + 1:]) + 1):
                	empty_domain.append(x)
                print("empty_domain",empty_domain) 
                
                i = 0
                range_y = []
                print("loop start")
                print(len(empty_domain))
                
                self.ids.list_of_steps.add_widget(Label(text= "Domain | Range" ,font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "x | y" ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                while i < len(empty_domain):
                    y_input = str(y).replace("x","*" + str(empty_domain[i])).replace("+*","+").replace("-*","-").replace("/*","/").replace("(*","(").replace("sqrt","math.sqrt").replace("pi","math.pi").replace("^","**").replace("sin","math.sin").replace("cos","math.cos").replace("tan","math.tan").replace("csc","mpmath.csc").replace("sec","mpmath.sec").replace("cot","mpmath.cot").replace("log","math.log").replace("e","math.e").replace("smath.ec","mp.sec").replace("math.smath.secc","mp.sec").replace("math.math","math").replace("mp.mp","mp")
                    if y_input[0] == "*":
                        y_input = y_input.replace("*"," ")
                    print("y_input",y_input)
                    y_input = y_input.replace("^","**")
                    y_solved = eval(y_input)
                    print("y_solved",y_solved)
                    range_y.append(y_solved)
                    
                    self.ids.list_of_steps.add_widget(Label(text= str(empty_domain[i]) + " | " + str(y_solved) ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    i = i + 1
                    
                print("range_y",range_y)
                    
            elif comma_count == 2 and y.count("x") > 0:
                print("domain",domain)
                
                domain_list = str(domain).split(",")
                print(domain_list)
                
                sequence_list = []
                for x in range(int(domain_list[0]),int(domain_list[1]),int(domain_list[2])):
                    sequence_list.append(x)
                print("sequence_list",sequence_list)    
                
                if y.count("x") > 0:
                    i = 0
                    range_y = []
                    print("loop start")
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Domain | Range" ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "x | y" ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    while i < len(sequence_list):
                        y_input = str(y).replace("x","*" + str(sequence_list[i])).replace("+*","+").replace("-*","-").replace("/*","/").replace("(*","(").replace("sqrt","math.sqrt").replace("pi","math.pi").replace("^","**").replace("sin","math.sin").replace("cos","math.cos").replace("tan","math.tan").replace("csc","mpmath.csc").replace("sec","mpmath.sec").replace("cot","mpmath.cot").replace("log","math.log").replace("e","math.e").replace("smath.ec","mp.sec").replace("math.smath.secc","mp.sec").replace("math.math","math").replace("mp.mp","mp")
                        if y_input[0] == "*":
                            y_input = y_input.replace("*","")
                        print("y_input",y_input)
                        y_input = y_input.replace("^","**")
                        y_solved = eval(y_input)
                        print("y_solved",y_solved)
                        range_y.append(y_solved)
                        
                        self.ids.list_of_steps.add_widget(Label(text= str(sequence_list[i]) + " | " + str(y_solved) ,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        
                        i = i + 1
                        
                    print("range_y",range_y)
                    
                else:
                    self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            else:
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)

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
                    text: "Menu"   
                    font_size: 75
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
        print()
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        print("entry",entry)
        display = entry.replace("$","^")
        entry_list = entry.split("$")
        print("display :" + display)
        self.ids.list_of_steps.add_widget(Label(text="Expression entered : " + display, font_size = 50, size_hint_y= None, height=100))
        Answer = str(eval(str(display).replace("^","**")))
        Answer = "{:,}".format(float(Answer.replace(",","")))
        print("Answer",Answer)
        self.ids.list_of_steps.add_widget(Label(text="Answer: " + '[color=33CAFF]' + Answer + '[/color]', markup=True, font_size = 50, size_hint_y= None, height=100))

        self.layouts.append(layout)
        
        try:
            entry = entry_list
            print("entry split: ",entry)
            print()
            
            base = entry_list[0]
            print("base",base)
            
            power = entry_list[1]
            print("power",power)
            
            if power.find("-") < 0:
                self.ids.list_of_steps.add_widget(Label(text="Proof of work:", font_size = 50, size_hint_y= None, height=100))
                
                i = 0
                product = base
                power_ = power
                while i < float(power_):
                    length = '[color=33CAFF]' + product + '[/color]' + " * " + base
                    print("length",length)
                    if int(power) > 1:
                        self.ids.list_of_steps.add_widget(Label(text= length ,font_size = 50, markup=True, size_hint_y= None, height=100))
                    else:
                        self.ids.list_of_steps.add_widget(Label(text= '[color=33CAFF]' + product + '[/color]', markup=True, font_size = 50, size_hint_y= None, height=100))
                    power = int(power) - 1
                    print("power",power)
                    product = "{:,}".format(float(product.replace(",","")) * float(base))
                    print("product",product)
                    i = i + 1
            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)  

#FOIL
Builder.load_string("""
<FOIL>
    id:FOIL
    name:"FOIL"
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
                text: "FOIL Method"
                    
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
                    font_size: 75
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
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        entry.text = ""
                        list_of_steps.clear_widgets()            
                    
            TextInput:
                id: entry
                text: entry.text
                multiline: False
                hint_text: "(ax + b)(cx + d)"
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10
                
            Button:
                markup: True
                id: steps
                text: "Calculate"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    FOIL.steps(entry.text)    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                  
                    
""")

class FOIL(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(FOIL, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            print("Its working ESC = 27 LENGTH")
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        print("Length is almost working")        
        if sm.current != "Homepage":
            print("Its working List")
            sm.transition.direction = 'right'
            sm.current = "Menu"
            
    layouts = []
    def steps(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            a = entry.lower()
            a = a.replace(" ","")
            a = a.replace("+-","-")
            a = a.replace(")*(",")(")
            a = a.replace("+"," + ")
            a = a.replace("-"," - ")
            a = a.replace("**","^")
            a = a.replace("( - ","(-")
            a = a.replace("*"," * ")
            
            # Split string method to Highlight each step in green before evaluation
            a_list = a.replace(")("," ").replace("(","").replace(")","")
            a_list = a_list.split(" ")
            print(a_list)
            
            print()
            print("Expression entered:  ",a)
            print()
            
            self.ids.list_of_steps.add_widget(Label(text= "Expression Entered: " + a ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            x = Symbol('x')
            a = a.replace("x","*x")
            
            i = 0
            if a.count("(") == a.count(")"):
            # String Method to find FIRST
                #print("FIRST")
                while i < 1:
                    #print(a)
                    first_left_par = a.find("(")
                    first_right_par = a.find(")")
                    second_left_par = a.rfind("(")
                    second_right_par = a.rfind(")")
                    if a == " / ":
                        print("Invalid Input, no division in or outside of parentheses for Foil Methed")
                        break
                    if a == " * ":
                        print("Invalid Input, no multiplication within parentheses for Foil Method")
                        break
                    
                    right_par_left_side = a.find(")")
                    #print('right_par_left_side',right_par_left_side)
                    left_par_left_side = a[:right_par_left_side].rfind("(")
                    #print('left_par_left_side',left_par_left_side)
                    left_par_range = a[left_par_left_side:right_par_left_side+1]
                    #print('left_par_range: ',left_par_range)
                    
                    j = 0
                    while j < 1:
                        if left_par_range == " + " or "+": #  Find Add Sign
                            first_sign = left_par_range.rfind("+")
                            if first_sign == -1:
                                break
                            #sign = left_par_range.rfind("-")
                            #print("add_sign index: ",first_sign)
                            First_left = a[left_par_left_side+1:first_sign-1]
                            print("First_left",First_left)
                            if First_left == "*x":
                                First_left = "1*x"
                            next_par_range = a[right_par_left_side+1:]
                            #print('next_par_range',next_par_range)
                            left_par_right_side = next_par_range[:].find("(")
                            #print('next_par index',left_par_right_side)
                            right_par_right_side = next_par_range[:].find(")") #First Right Par
                            #print('right_par_right_side',right_par_right_side)
                            first_space_index = next_par_range[:].find(" ")
                            #print('first_space_index',first_space_index)
                            First_right = next_par_range[left_par_right_side+1:first_space_index+1]
                            print('First_right',First_right)# Use for Highlight
                            if First_right == "*x ":
                                First_right = "1*x"
                            #print()
                            #print("First Type ",type(First))
                            FIRST_DISPLAY = "FIRST: (" + '[color=33CAFF]' + str(a_list[0]).replace("[","").replace("]","").replace("'","") + '[/color]' + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")(" + '[color=33CAFF]' + str(a_list[3]).replace("[","").replace("]","").replace("'","") + '[/color]' + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")"
                            self.ids.list_of_steps.add_widget(Label(text= FIRST_DISPLAY , markup=True, font_size = 50, size_hint_y= None, height=100))
                            print('FIRST                ',"(" + Back.GREEN + str(a_list[0]).replace("[","").replace("]","").replace("'","") + Style.RESET_ALL + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")(" + Back.GREEN + str(a_list[3]).replace("[","").replace("]","").replace("'","") + Style.RESET_ALL + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")")         #print("First Type ",type(First))
                            print()
                            First = First_left + " * " + First_right
                            First = First.replace("+-","-").replace("^","**")
                            #print("First Type ",type(First))
                            #First = sympify(First)
                            #print('type',type(First))
                            First = str(First).replace("^","**")
                            print("First",First)
                            First_evaled = str(eval(First))
                            First = str(First).replace("**","^").replace("*-"," * -")
                            
                            FIRST_MULTIPLY = "Multiply: " + First.replace("*x","x").replace("**","^").replace("*"," * ") + " = " + '[color=33CAFF]' + First_evaled.replace("*x","x").replace("**","^") + '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= FIRST_MULTIPLY , markup=True, font_size = 50, size_hint_y= None, height=100))

                            print("Multiply:            ", First.replace("*x","x").replace("**","^").replace("*"," * ")," = ",Back.GREEN,First_evaled,Style.RESET_ALL)   
                            print()
                            #print('                  ',First_evaled)
                            highlight_first = First_evaled.replace("**","^").replace("*","").replace("-+","-")
                            print('Expression:          ',Back.BLUE,highlight_first,Style.RESET_ALL)
                            
                            FIRST_EXPRESSION = 'Expression: ' + '[color=33CAFF]' + highlight_first + "[/color]"
                            self.ids.list_of_steps.add_widget(Label(text= FIRST_EXPRESSION , markup=True, font_size = 50, size_hint_y= None, height=100))
                            
                            print()
                            self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' , markup=True, font_size = 50, size_hint_y= None, height=100))
                            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~') 
                            print()
                            
                            break
                    if first_sign == -1: #  Find Minus Sign
                        first_sign = left_par_range.rfind("-")
                        #sign = left_par_range.find("+")
                        #print("minus_sign index: ",first_sign)
                        First_left = a[left_par_left_side+1:first_sign-1]
                        if First_left == "*x":
                            First_left = "-1*x"
                        #print('First_left',First_left) # Use for Highlight
                        next_par_range = a[right_par_left_side+1:]
                        #print('next_par_range',next_par_range)
                        left_par_right_side = next_par_range[:].find("(")
                        #print('next_par index',left_par_right_side)
                        right_par_right_side = next_par_range[:].find(")") #First Right Par
                        #print('right_par_right_side',right_par_right_side)
                        first_space_index = next_par_range[:].find(" ")
                        #print('first_space_index',first_space_index)
                        First_right = next_par_range[left_par_right_side+1:first_space_index+1]
                        if First_right == "*x":
                            First_right = "-1*x"
                        #print('First_right',First_right)# Use for Highlight
                        #print()
                        First = First_left + " * " + First_right
                        print('FIRST                ',"(" + Back.GREEN + str(a_list[0]).replace("[","").replace("]","").replace("'","") + Style.RESET_ALL + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")(" + Back.GREEN + str(a_list[3]).replace("[","").replace("]","").replace("'","") + Style.RESET_ALL + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")")         #print("First Type ",type(First))
                        FIRST_DISPLAY = "FIRST: (" + '[color=33CAFF]' + str(a_list[0]).replace("[","").replace("]","").replace("'","") + '[/color]' + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")(" + '[color=33CAFF]' + str(a_list[3]).replace("[","").replace("]","").replace("'","") + '[/color]' + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")"
                        self.ids.list_of_steps.add_widget(Label(text= FIRST_DISPLAY , markup=True, font_size = 50, size_hint_y= None, height=100))

                        #print('type',type(First))
                        First = str(First).replace(" ","").replace("+-","-").replace('--',"+").replace("-+","-").replace("^","**")
                        #x,y,z = symbols('x,y,z')
                        First_evaled = str(eval(First))
                        print()
                        First = str(First).replace("**","^").replace("*-"," * -")
                        First_evaled = First_evaled.replace("**","^")
                        
                        FIRST_MULTIPLY = "Multiply: " + First.replace("*x","x").replace("**","^").replace("*"," * ") + " = " + '[color=33CAFF]' + First_evaled.replace("*x","x").replace("**","^") + '[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= FIRST_MULTIPLY , markup=True, font_size = 50, size_hint_y= None, height=100))

                        print("Multiply:            ", First.replace("*x","x").replace("**","^").replace("*"," * ")," = ",Back.GREEN,First_evaled,Style.RESET_ALL)  
                        print()
                        #print('                  ',First_evaled)
                        highlight_first = First_evaled.replace("**","^").replace("*","")
                        #print()
                        print('Expression:          ',Back.BLUE,highlight_first,Style.RESET_ALL)
                        
                        FIRST_EXPRESSION = 'Expression: ' + '[color=33CAFF]' + highlight_first + "[/color]"
                        self.ids.list_of_steps.add_widget(Label(text= FIRST_EXPRESSION , markup=True, font_size = 50, size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' , markup=True, font_size = 50, size_hint_y= None, height=100))
                        
                        print()
                        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                        print()
                            
                        break
                    i = i + 1
            # String method for OUTSIDE
                i = 0
                while i < 1:
                    if next_par_range == "+" or  "-":
                        sign_index = next_par_range.find("+")
                        if sign_index == -1:
                            sign_index = next_par_range.rfind("-")
                        #print('sign_index',sign_index)
                    Outside_right = next_par_range[sign_index:right_par_right_side]
                    Outside_right = Outside_right.replace("+","").replace(" ","").strip()
                    #print("Outside_right",Outside_right)
                    if Outside_right == "*x":
                        Outside_right = "1*x"
                    elif Outside_right == "+ *x":
                        Outside_right = "1*x"
                    elif Outside_right == "- *x":
                        Outside_right = "-1*x"
                    Outside = First_left + " * " + Outside_right
                    print('OUTSIDE              ',"(" + Back.GREEN + str(a_list[0]).replace("[","").replace("]","").replace("'","") + Style.RESET_ALL + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")(" + str(a_list[3]).replace("[","").replace("]","").replace("'","") + Back.GREEN + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + Style.RESET_ALL + ")")         #print("First Type ",type(First))
                    
                    OUTSIDE_DISPLAY = "OUTSIDE: (" + '[color=33CAFF]' + str(a_list[0]).replace("[","").replace("]","").replace("'","") + '[/color]' + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")(" + str(a_list[3]).replace("[","").replace("]","").replace("'","") + '[color=33CAFF]' + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + '[/color]' + ")"
                    self.ids.list_of_steps.add_widget(Label(text= OUTSIDE_DISPLAY , markup=True, font_size = 50, size_hint_y= None, height=100))
                    
                    evaled_Outside = str(Outside).replace("^","**")
                    evaled_Outside = eval(evaled_Outside)
                    Outside = Outside.replace("^","**")
                    evaled_Outside = str(evaled_Outside).replace("**","^")
                    print()
                    print("Multiply:            ",Outside.replace("**","^").replace("*x","x")," = ",Back.GREEN,evaled_Outside,Style.RESET_ALL)
                    
                    OUTSIDE_MULTIPLY = "Multiply: " + Outside.replace("**","^").replace("*x","x") + " = " + '[color=33CAFF]' + evaled_Outside + '[/color]'
                    self.ids.list_of_steps.add_widget(Label(text= OUTSIDE_MULTIPLY , markup=True, font_size = 50, size_hint_y= None, height=100))
                    
                    #print()
                    #print('evaled_Outside',evaled_Outside)
                    #print()
                    highlight_Outside = str(evaled_Outside).replace(" ","").replace("**","^").replace("*","").replace("-"," - ").strip()
                    
                    if highlight_Outside[0] != "-":
                        highlight_Outside = " + " + highlight_Outside
                    print()
                    print("Expression:          ",Back.BLUE,highlight_first,Style.RESET_ALL,Back.GREEN,highlight_Outside,Style.RESET_ALL)
                    
                    OUTSIDE_HIGHLIGHT = "Expression: " + '[color=33CAFF]'  + highlight_first + highlight_Outside + '[/color]'
                    self.ids.list_of_steps.add_widget(Label(text= OUTSIDE_HIGHLIGHT , markup=True, font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' , markup=True, font_size = 50, size_hint_y= None, height=100))
                    
                    print()
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print()
                    
                    break
            
            # String Method for INSIDE
                i = 0
                while i < 1:        
                    INSIDE_left = left_par_range[first_sign:right_par_left_side]
                    INSIDE_left = INSIDE_left.replace("^","**")
                    print(INSIDE_left)
                    if INSIDE_left == "+ *x":
                        INSIDE_left = "1*x"
                    elif INSIDE_left == "- *x":
                        INSIDE_left = "-1*x"
                    Inside_sign = left_par_range.find("+")
                    if Inside_sign == -1:
                        Inside_sign = left_par_range.rfind("-")
                        
                    #print("INSIDE_left",INSIDE_left) 
                    #print("Inside_sign index",Inside_sign)
                    Inside_sign_right_side = next_par_range.find("+")
                    if Inside_sign_right_side == -1:
                        Inside_sign_right_side = next_par_range.rfind("-")
                    print('INSIDE               ',"(" + str(a_list[0]).replace("[","").replace("]","").replace("'","") + Back.GREEN + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + Style.RESET_ALL + ")(" + Back.GREEN + str(a_list[3]).replace("[","").replace("]","").replace("'","") + Style.RESET_ALL + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + Style.RESET_ALL + ")")         #print("First Type ",type(First))
                    
                    INSIDE_DISPLAY = "INSIDE (" + str(a_list[0]).replace("[","").replace("]","").replace("'","") + '[color=33CAFF]' + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + '[/color]' + ")(" + '[color=33CAFF]' + str(a_list[3]).replace("[","").replace("]","").replace("'","") + '[/color]' + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + '[/color]' + ")"
                    self.ids.list_of_steps.add_widget(Label(text= INSIDE_DISPLAY , markup=True, font_size = 50, size_hint_y= None, height=100))

                    Inside =  INSIDE_left + " * " + First_right
                    Inside = Inside.replace("^","**")
                    if Inside == "*x":
                        Inside = "1*x"
                    print()
                    Inside_evaled = str(eval(Inside)).replace(" ","").replace("**","^").replace("+"," +").strip()
                    Inside = Inside.replace("**","^")
                    Inside_evaled = str(Inside_evaled).replace("**","^")
                    Inside_evaled = Inside_evaled.replace("+-","-")
                    print("Multiply:            ",Inside.replace("*x","x").replace("**","^")," = ",Back.GREEN,Inside_evaled,Style.RESET_ALL)
                    print()
                    
                    INSIDE_MULTIPLY = "Multiply: " + Inside.replace("*x","x").replace("**","^") + " = " + '[color=33CAFF]' + Inside_evaled + '[/color]'
                    self.ids.list_of_steps.add_widget(Label(text= INSIDE_MULTIPLY , markup=True, font_size = 50, size_hint_y= None, height=100))
                    
                    #print("Inside_evaled",Inside_evaled)
                    highlight_Inside = Inside_evaled.replace("*","").replace(" ","")

                    if highlight_Inside[0] != "-":
                        highlight_Inside = " + " + highlight_Inside
                    print("Expression:         ",Back.BLUE,highlight_first,highlight_Outside,Style.RESET_ALL,Back.GREEN,highlight_Inside,Style.RESET_ALL)
                    
                    INSIDE_HIGHLIGHT = "Expression: " + '[color=33CAFF]' + highlight_first + highlight_Outside + highlight_Inside + '[/color]'
                    self.ids.list_of_steps.add_widget(Label(text= INSIDE_HIGHLIGHT , markup=True, font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' , markup=True, font_size = 50, size_hint_y= None, height=100))
                    print()
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print()
                    break
                
            # String Method for LAST
                i = 0 
                while i < 1:
                    print('LAST                 ',"(" + str(a_list[0]).replace("[","").replace("]","").replace("'","") + Back.GREEN + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + Style.RESET_ALL + ")(" + str(a_list[3]).replace("[","").replace("]","").replace("'","") + Back.GREEN + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + Style.RESET_ALL + ")")         #print("First Type ",type(First))
                    print()
                    
                    LAST_DISPLAY = "LAST: (" + str(a_list[0]).replace("[","").replace("]","").replace("'","") + '[color=33CAFF]' + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + '[/color]' + ")(" + str(a_list[3]).replace("[","").replace("]","").replace("'","") + '[color=33CAFF]' + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + '[/color]' + ")"
                    self.ids.list_of_steps.add_widget(Label(text= LAST_DISPLAY , markup=True, font_size = 50, size_hint_y= None, height=100))

                    Last = INSIDE_left + " * " + Outside_right 
                    Last = Last.replace("^","**")
                    if Last == "*x":
                        Last = "1*x"
                    Last_evaled = str(eval(Last)).replace(" ","").replace("**","^").replace("-","- ").strip()
                    Last = Last.replace("^","**")
                    Last_evaled = str(Last_evaled).replace("**","^")
                    print("Multiply:            ",Last.replace("*x","x").replace("**","^")," = ",Back.GREEN,Last_evaled,Style.RESET_ALL)
                    print()
                    #print('Last_evaled',Last_evaled)
                    
                    LAST_MULTIPLY = "Multiply: " + Last.replace("*x","x").replace("**","^") + " = " + '[color=33CAFF]' + Last_evaled + '[/color]'
                    self.ids.list_of_steps.add_widget(Label(text= LAST_MULTIPLY , markup=True, font_size = 50, size_hint_y= None, height=100))
                    
                    highlight_Last = Last_evaled.replace("*","")#.replace("-","- ")
            
                    if highlight_Last[0] != "-":
                        highlight_Last = " + " + highlight_Last
            
                    print("Expression:         ",Back.BLUE,highlight_first,highlight_Outside,highlight_Inside,Style.RESET_ALL,Back.GREEN,highlight_Last,Style.RESET_ALL)
                    LAST_EXPRESSION = "Expression: " + '[color=33CAFF]' + highlight_first + highlight_Outside + highlight_Inside + highlight_Last + '[/color]'
                    self.ids.list_of_steps.add_widget(Label(text= LAST_EXPRESSION , markup=True, font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' , markup=True, font_size = 50, size_hint_y= None, height=100))
                    print()
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print()        
                    break
                
                FOIL = str(First_evaled) + "+" + str(evaled_Outside) + "+" + str(Inside_evaled) + "+" + str(Last_evaled)
                FOIL = FOIL.strip().replace("**","^").replace(" ","").replace("+-","-").replace("+"," + ").replace("-"," - ").replace("*","")
                print("Expression FOILed:  ",Back.BLUE,FOIL,Style.RESET_ALL)
                EXPRESSION_FOLIED = '[color=33CAFF]' + FOIL + '[/color]'
                self.ids.list_of_steps.add_widget(Label(text= "Expression FOILed:  ", markup=True, font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= EXPRESSION_FOLIED , markup=True, font_size = 50, size_hint_y= None, height=100))
                print()
                self.ids.list_of_steps.add_widget(Label(text= "Next, combine like terms" , markup=True, font_size = 50, size_hint_y= None, height=100))
                print("Next, combine like terms")
                print()
                self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' , markup=True, font_size = 50, size_hint_y= None, height=100))
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print()  
                
                First_evaled = str(First_evaled).replace("^","**")
                evaled_Outside = "+" + str(evaled_Outside).replace("^","**")
                Inside_evaled =  "+" + str(Inside_evaled).replace("^","**")
                Last_evaled =  "+" + str(Last_evaled).replace("^","**")
                First_evaled =  str(First_evaled).replace("+-","-")
                evaled_Outside = str(evaled_Outside).replace("+-","-")
                Inside_evaled =   str(Inside_evaled).replace("+-","-")
                Last_evaled =  str(Last_evaled).replace("+-","-")
                
                #print("aLL CURRENTLY    ",First_evaled," ",evaled_Outside," ",Inside_evaled," ",Last_evaled)
                answer = ""
                combine_evaled_FOIL = ""
                combine_evaled_FO = ""
                combine_evaled_IL = ""
                combine_evaled_FI = ""
                combine_evaled_OL = ""
                combine_evaled_FL = ""
                combine_evaled_OI = ""
            # Combine Like Terms if all can combine
            
                
            #Combine like Terms
            #First evaled, check for if Exponent, Variable, Integer
                First_evaled = First_evaled.replace("**","^")
                evaled_Outside = evaled_Outside.replace("**","^")
                Inside_evaled = Inside_evaled.replace("**","^")
                Last_evaled = Last_evaled.replace("**","^")
                
                exponent_First_evaled = " "
                variable_First_evaled = " "
                integer_First_evaled = " "
                
                exponent_evaled_Outside = " "
                variable_Outside_evaled = " "
                integer_evaled_Outside = " "
                
                exponent_Inside_evaled = " "
                variable_Inside_evaled = " "
                integer_Inside_evaled = " "
                
                exponent_Last_evaled = " "
                variable_Last_evaled = " "
                integer_Last_evaled = " "
                
                non_combine = 0
                
                i = 0
                while i < 1: #Highlight each possible combo
                    if First_evaled.count("^") == 1:
                        exponent_First_evaled = First_evaled.replace("^","**")
                        print(First_evaled.replace("*",""),"is an exponent")
                        carrot = First_evaled.find("^")
                        exponent_First = First_evaled[carrot+1:]
                        print("exponent_First",exponent_First)
                        
                    if evaled_Outside.count("^") == 1:
                        exponent_evaled_Outside = evaled_Outside.replace("^","**")
                        print(evaled_Outside, "Its an exponent")
                        carrot = evaled_Outside.find("^")
                        exponent_Outside = evaled_Outside[carrot+1:]
                        print("exponent_First",exponent_Outside)
                        
                    if Inside_evaled.count("^") == 1:
                        exponent_Inside_evaled = Inside_evaled.replace("^","**")
                        print(Inside_evaled,"Its an exponent")
                        carrot = Inside_evaled.find("^")
                        exponent_Inside = Inside_evaled[carrot+1:]
                        print("exponent_First",exponent_Inside)
                        
                    if Last_evaled.count("^") == 1:
                        exponent_Last_evaled = Last_evaled.replace("^","**")
                        print(Last_evaled,"Its an exponent")
                        carrot = Last_evaled.find("^")
                        exponent_Last = Last_evaled[carrot+1:]
                        print("exponent_First",exponent_Last)
                    
                    if exponent_First_evaled != " " and exponent_evaled_Outside  != " " and exponent_Inside_evaled != " " and exponent_Last_evaled != " ":
                        print("1Combine terms:      ",Back.BLUE,First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + "),evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "),Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "),Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "),Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: " + '[color=33CAFF]' + First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ") + evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[/color]' 
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     ",Back.BLUE,str(eval(exponent_First_evaled + exponent_evaled_Outside + exponent_Inside_evaled + exponent_Last_evaled)).replace("*","").replace("**","^"),Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: " + '[color=33CAFF]' + str(eval(exponent_First_evaled + exponent_evaled_Outside + exponent_Inside_evaled + exponent_Last_evaled)).replace("**","^").replace("**","^") + '[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                        break
                    if exponent_First_evaled != " " and exponent_evaled_Outside  != " ":
                        print()
                        print("exponent_First_evaled",exponent_First_evaled)
                        print("exponent_evaled_Outside",exponent_evaled_Outside)
                        print()
                        if exponent_First_evaled[-1] == exponent_evaled_Outside[-1]:
                            print("2Combine terms:      ",Back.BLUE,First_evaled.replace(" ","").replace("**","^").replace("*",""),evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "),Style.RESET_ALL,Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "),Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                            COMBINE_TERMS = "Combine terms: " + '[color=33CAFF]' + First_evaled.replace(" ","").replace("**","^").replace("*",""),evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[/color]' + Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                            self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                            print()
                            print("Terms Combined:     ",Back.BLUE,str(eval(exponent_First_evaled +" + "+ exponent_evaled_Outside)).replace("**","^").replace("*"," "),Style.RESET_ALL)
                            COMBINED_TERMS_EVALED = "Terms Combined: " + '[color=33CAFF]' + str(eval(exponent_First_evaled +" + "+ exponent_evaled_Outside)).replace("**","^").replace("*"," ") + '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                            print()
                            non_combine = non_combine - 1
                    if exponent_First_evaled != " " and exponent_Inside_evaled  != " ":
                        print()
                        print("exponent_First_evaled",exponent_First_evaled)
                        print("exponent_Inside_evaled",exponent_Inside_evaled)
                        print()
                        if exponent_First_evaled[-1] == exponent_Inside_evaled[-1]:
                            print("3Combine terms: "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Style.RESET_ALL+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                            COMBINE_TERMS = "Combine terms: "+ '[color=33CAFF]' + First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ") + '[/color]' + evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[color=33CAFF]' + Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[/color]' + Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                            self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                            print()
                            print("Terms Combined:     "+Back.BLUE+str(eval(exponent_First_evaled +" + "+ exponent_Inside_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                            COMBINED_TERMS_EVALED = "Terms Combined: " + '[color=33CAFF]' + str(eval(exponent_First_evaled +" + "+ exponent_evaled_Outside)).replace("**","^").replace("*"," ") + '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                            print()
                            non_combine = non_combine - 1
                    if exponent_First_evaled != " " and exponent_Last_evaled  != " ":
                        print()
                        print("exponent_First_evaled",exponent_First_evaled)
                        print("exponent_Last_evaled",exponent_Last_evaled)
                        print()
                        if exponent_First_evaled[-1] == exponent_Last_evaled[-1]:
                            print("4Combine terms: "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Style.RESET_ALL+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                            COMBINE_TERMS = "Combine terms: " + '[color=33CAFF]' + First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ") + '[/color]' + evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[/color]' + Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                            print()
                            print("Terms Combined:     "+Back.BLUE+str(eval(exponent_First_evaled +" + "+ exponent_Last_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                            COMBINED_TERMS_EVALED = "Terms Combined: " + '[color=33CAFF]' + str(eval(exponent_First_evaled +" + "+ exponent_evaled_Outside)).replace("**","^").replace("*"," ") + '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                            print()
                            non_combine = non_combine - 1
                    if exponent_evaled_Outside != " " and exponent_Inside_evaled  != " ":
                        print()
                        print("exponent_evaled_Outside",exponent_evaled_Outside)
                        print("exponent_Inside_evaled",exponent_Inside_evaled)
                        print()
                        if exponent_First_evaled[-1] == exponent_Last_evaled[-1]:
                            print("5Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Back.BLUE+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                            COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+ '[color=33CAFF]' +evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+ '[/color]' +Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                            self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                            print()
                            print("Terms Combined:     "+Back.BLUE+str(eval(exponent_evaled_Outside +" + "+ exponent_Inside_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                            COMBINED_TERMS_EVALED = "Terms Combined: "+ '[color=33CAFF]' +str(eval(exponent_evaled_Outside +" + "+ exponent_Inside_evaled)).replace("*","").replace("**","^")+'[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                            print()
                            non_combine = non_combine - 1
                    if exponent_evaled_Outside != " " and exponent_Last_evaled != " ":
                        print()
                        print("exponent_evaled_Outside",exponent_evaled_Outside)
                        print("exponent_Last_evaled",exponent_Last_evaled)
                        print()
                        if exponent_First_evaled[-1] == exponent_Last_evaled[-1]:
                            print("6Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Back.BLUE+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                            COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+ '[color=33CAFF]' +evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+ '[/color]' +Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[color=33CAFF]' + Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                            print()
                            print("Terms Combined:     "+Back.BLUE+str(eval(exponent_evaled_Outside +" + "+ exponent_Last_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                            COMBINED_TERMS_EVALED = "Terms Combined: "+ '[color=33CAFF]' +str(eval(exponent_evaled_Outside +" + "+ exponent_Last_evaled)).replace("*","").replace("**","^")+ '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                            print()
                            non_combine = non_combine - 1
                    if exponent_Inside_evaled != " " and exponent_Last_evaled != " ":
                        print()
                        print("exponent_Inside_evaled",exponent_Inside_evaled)
                        print("exponent_Last_evaled",exponent_Last_evaled)
                        print()
                        if exponent_First_evaled[-1] == exponent_Last_evaled[-1]:
                            print("7Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)        
                            COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                            print()
                            print("Terms Combined:     "+Back.BLUE+str(eval(exponent_Inside_evaled +" + "+ exponent_Last_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                            COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]' + str(eval(exponent_Inside_evaled +" + "+ exponent_Last_evaled)).replace("*","").replace("**","^")+ '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                            print()
                            non_combine = non_combine - 1
                    non_combine = non_combine + 1
                    break
                i = 0
                while i < 1:
                    if First_evaled.count("x") == 1 and First_evaled.count("^") == 0:
                        variable_First_evaled = First_evaled
                        print("Its a variable F"+variable_First_evaled)
                    if evaled_Outside.count("x") == 1 and evaled_Outside.count("^") == 0:
                        variable_Outside_evaled = evaled_Outside
                        print("Its a variable O"+variable_Outside_evaled)
                    if Inside_evaled.count("x") == 1 and Inside_evaled.count("^") == 0:
                        variable_Inside_evaled = Inside_evaled
                        print("Its a variable I"+variable_Inside_evaled)
                    if Last_evaled.count("x") == 1 and Last_evaled.count("^") == 0:
                        variable_Last_evaled = Last_evaled
                        print("Its a variable L"+variable_Last_evaled)
            
                    if variable_First_evaled != " " and variable_Outside_evaled  != " " and variable_Inside_evaled != " " and variable_Last_evaled != " ":
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+'[color=33CAFF]'+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+ '[/color]' 
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_First_evaled +" + "+ variable_Outside_evaled +" + "+ variable_Inside_evaled +" + "+ variable_Last_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_First_evaled +" + "+ variable_Outside_evaled +" + "+ variable_Inside_evaled +" + "+ variable_Last_evaled)).replace("*","").replace("**","^")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                        break
                    if variable_First_evaled != " " and variable_Outside_evaled != " " :
                        print()
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                        COMBINE_TERMS = "Combine terms: "+'[color=33CAFF]'+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_First_evaled +" + "+ variable_Outside_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_First_evaled +" + "+ variable_Outside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if variable_First_evaled != " " and variable_Inside_evaled != " " :
                        print()
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Style.RESET_ALL+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                        COMBINE_TERMS = "Combine terms: "+'[color=33CAFF]'+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[/color]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_First_evaled +" + "+ variable_Inside_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_First_evaled +" + "+ variable_Inside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if variable_First_evaled != " " and variable_Last_evaled != " " :
                        print()
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Style.RESET_ALL+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+'[color=33CAFF]'+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[/color]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_First_evaled +" + "+ variable_Last_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_First_evaled +" + "+ variable_Last_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if variable_Outside_evaled != " " and variable_Inside_evaled != " " :
                        print()
                        print("Combine terms:      "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Back.BLUE+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_Outside_evaled +" + "+ variable_Inside_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_Outside_evaled +" + "+ variable_Inside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if variable_Outside_evaled != " " and variable_Last_evaled != " " :
                        print()
                        print("Combine terms:      "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Back.BLUE+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_Outside_evaled +" + "+ variable_Last_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_Outside_evaled +" + "+ variable_Inside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if variable_Inside_evaled != " " and variable_Last_evaled != " " :
                        print()
                        print("Combine terms:      "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_Inside_evaled +" + "+ variable_Last_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_Inside_evaled +" + "+ variable_Last_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                        break
                    non_combine = non_combine + 1
                    break
            
                i = 0
                while i < 1:
                    if First_evaled.count("x") == 0 and First_evaled.count("^") == 0:
                        integer_First_evaled =  First_evaled
                        print("Its an integer F")
                    if evaled_Outside.count("x") == 0 and evaled_Outside.count("^") == 0:
                        integer_evaled_Outside =  evaled_Outside
                        print("Its an integer O")
                    if Inside_evaled.count("x") == 0 and Inside_evaled.count("^") == 0:
                        integer_Inside_evaled =  Inside_evaled
                        print("Its an integer I")
                    if Last_evaled.count("x") == 0 and Last_evaled.count("^") == 0:
                        integer_Last_evaled =  Last_evaled
                        print("Its an integer L")
                      
                    if integer_First_evaled != " " and integer_evaled_Outside  != " " and integer_Inside_evaled != " " and integer_Last_evaled != " ":
                        print("FOIL")
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_First_evaled +" + "+ integer_evaled_Outside +" + "+ integer_Inside_evaled +" + "+ integer_Last_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_First_evaled +" + "+ integer_evaled_Outside +" + "+ integer_Inside_evaled +" + "+ integer_Last_evaled)).replace("*","").replace("**","^")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                        break
                    if integer_First_evaled != " " and integer_evaled_Outside != " " :
                        print()
                        print("FO")
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_First_evaled +" + "+ integer_evaled_Outside)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_First_evaled +" + "+ integer_evaled_Outside)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if integer_First_evaled != " " and integer_Inside_evaled != " " :
                        print()
                        print("FI")
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Style.RESET_ALL+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                        COMBINE_TERMS = "Combine terms: "+'[color=33CAFF]'+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[/color]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_First_evaled +" + "+ integer_Inside_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_First_evaled +" + "+ integer_Inside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if integer_First_evaled != " " and integer_Last_evaled != " " :
                        print()
                        print("FL")
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Style.RESET_ALL+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+'[color=33CAFF]'+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[/color]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_First_evaled +" + "+ integer_Last_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_First_evaled +" + "+ integer_Last_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if integer_evaled_Outside != " " and integer_Inside_evaled != " " :
                        print()
                        print("OI")
                        print("Combine terms:      "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Back.BLUE+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_evaled_Outside +" + "+ integer_Inside_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_evaled_Outside +" + "+ integer_Inside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if integer_evaled_Outside != " " and integer_Last_evaled != " " :
                        print()
                        print("OL")
                        print("Combine terms:      "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Back.BLUE+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_evaled_Outside +" + "+ integer_Last_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_evaled_Outside +" + "+ integer_Inside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if integer_Inside_evaled != " " and integer_Last_evaled != " " :
                        print()
                        print("IL")
                        print("Combine terms:      "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)        
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'  
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_Inside_evaled +" + "+ integer_Last_evaled)).replace("*"+"")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_Inside_evaled +" + "+ integer_Last_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 50, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    non_combine = non_combine + 1
                    break
                
                if non_combine == 3:
                    print("No terms to combine")
                    self.ids.list_of_steps.add_widget(Label(text= "No terms to combine" , markup=True, font_size = 50, size_hint_y= None, height=100))
                    
                exponents_evaled_list = [exponent_First_evaled,exponent_evaled_Outside,exponent_Inside_evaled,exponent_Last_evaled]
                #print("exponents_evaled_list",exponents_evaled_list)
                #print()
                add_up_exponents = exponent_First_evaled + exponent_evaled_Outside + exponent_Inside_evaled + exponent_Last_evaled
                add_up_exponents = add_up_exponents.replace(" ","").replace("**","^")
                combined_exponents = ""
                if add_up_exponents.count("^") > 0:
                    add_up_exponents = add_up_exponents.replace("^","**").replace(" ","")
                    combined_exponents = str(eval(add_up_exponents)).replace("**","^")
                #print(combined_exponents.replace("**","^").replace("*",""))
                
                First_evaled_exp_index = exponent_First_evaled.find("^")
                #print("First_evaled_exp_index",First_evaled_exp_index)
                
                #print()
                variables_evaled_list = [variable_First_evaled,variable_Outside_evaled,variable_Inside_evaled,variable_Last_evaled]
                #print("variables_evaled_list",variables_evaled_list)
                #print()
                add_up_variables = variable_First_evaled + variable_Outside_evaled + variable_Inside_evaled + variable_Last_evaled
                add_up_variables = add_up_variables.strip().replace(" ","")
                combined_variables = ""
                if add_up_variables.count("x") > 0:
                    combined_variables = str(eval(add_up_variables))
                #print("combined_variables",combined_variables)
                #print()
                
                #integers_evaled_list = [integer_First_evaled,integer_evaled_Outside,integer_Inside_evaled,integer_Last_evaled]
                #print("integers_evaled_list",integers_evaled_list)
                #print()
                add_up_integers = integer_First_evaled + integer_evaled_Outside + integer_Inside_evaled + integer_Last_evaled
                #print("add_up_integers length",len(add_up_integers.replace(" ","")))
                combined_integers = ""
                add_up_integers = add_up_integers.strip().replace(" ","")
                if len(add_up_integers.replace(" ","")) != 0:
                   combined_integers = str(eval(add_up_integers))
                #print("combined_variables",combined_integers)
                
                FINAL_ANSWER = (str(combined_exponents) + "+" + str(combined_variables) + "+" + str(combined_integers)).replace("*","").replace("++","")
                print("FINAL_ANSWER: ",FINAL_ANSWER)
                if FINAL_ANSWER[-1] == "+" or FINAL_ANSWER[-1] == "-":
                    FINAL_ANSWER = FINAL_ANSWER[:-1]
                FINAL_ANSWER = FINAL_ANSWER.replace("+-","-").replace("-"," - ").replace("+"," + ").replace("*","")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print()
                print("Answer in order:    ",FINAL_ANSWER)
                self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' ,font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Final Answer: " + FINAL_ANSWER.replace("*","") ,font_size = 50, size_hint_y= None, height=100))
                
            else:
                print("Parentheses Unbalanced")
            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)

#PEMDAS
Builder.load_string("""
<PEMDAS>
    id:PEMDAS
    name:"PEMDAS"
    
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
                text: "PEMDAS"
                
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
                    text: "Menu"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        entry.text = ""
                        list_of_steps.clear_widgets() 
            
            TextInput:
                id: entry
                text: entry.text
                hint_text: "Enter expression:"
                multiline: False
                font_size: 100
                size_hint_y: None
                height: 200
                padding: 10
            
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
                    PEMDAS.steps(entry.text)    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class PEMDAS(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(PEMDAS, self).__init__(**kwargs)
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
        
        
        try:
            #Parentheses
            a = entry
            a = a.strip()
            a = a.replace(" ","").replace("÷","/").replace("×","*")
            print(a)
            print()
            print("------------------------------")
            print()
            
            a = a.replace(" ","")
            a = a.replace("+-","-")
            a = a.replace("-+","-")
            a = a.replace("+"," + ")
            a = a.replace("-"," - ")
            a = a.replace("**", "^")
            a = a.replace("*"," * ")
            a = a.replace("/"," / ")
            a = a.replace(" ^ - ","^-")
            a = a.replace("^*","^")
            a = a.replace("*(","(")
            a = a.replace("* (","(")
            a = a.replace("(","*(")
            a = a.replace("+ *(","+ (")
            a = a.replace("- *(","- (")
            a = a.replace("^*","^")
            a = a.replace("/ *","/")
            
            
            if a[0] == "*":
                a = a[1:]
                print("a =",a)
            
            
            print("Expression Entered :      ",a)
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
            self.ids.list_of_steps.add_widget(Label(text="Expression entered : ", font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= entry, font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            #String Method to look for Parentheses
            if a.count("(") == a.count(")") and a.count("(") > 0 and a.count("(") > 0:
                  i = 0
                  while i < len(a):
                    right_par = a.find(")")
                    left_par = a[:right_par].rfind("(")
                    if right_par and left_par == -1:
                        print("breaking loop, no pars")
                        break
                    range_pars = a[left_par:right_par+1]
                    range_pars = range_pars.replace("^","**")
                    print(range_pars)
                    evaled = eval(range_pars)
                    evaled = str(evaled)
                    print(evaled)
                    range_pars = range_pars.replace("**","^")
                    if a.count("(") and a.count(")") == 0:
                        print("breaking loop, a.count(()) = 0")
                        break
                    print()
                    print()
                    print("Parentheses to Solve :    ",a[:left_par],Back.GREEN,range_pars,Style.RESET_ALL,a[right_par+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Parentheses Step : " , font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:left_par] + '[color=33CAFF]' + range_pars + '[/color]' + a[right_par+1:],markup=True, font_size = 50, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    replaced = a.replace(range_pars,evaled)
                    print()
                    print("Parentheses Solved :      ",a[:left_par],Back.GREEN,evaled,Style.RESET_ALL,a[right_par+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Parentheses Solved : " , font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:left_par] + '[color=33CAFF]' + evaled + '[/color]' + a[right_par+1:],markup=True, font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = 50, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    print("replaced to a:",replaced)
                    a = replaced
                    print("a =",a)
                    i = i + 1 
            
            elif a.count("(") == 0 and a.count(")") == 0:
                print("No Parenthesis, continue to exponents step")
                
            else:
                print("Parentheses Unbalanced!")
            
            
            a = a.replace(" ","")
            a = a.replace("+-","-")
            a = a.replace("-+","-")
            a = a.replace("+"," + ")
            a = a.replace("-"," - ")
            a = a.replace("**", "^")
            a = a.replace("*"," * ")
            a = a.replace("/"," / ")
            a = a.replace(" ^ - ","^-")
            a = a.replace("^*","^")
            a = a.replace("* (","(")
            a = a.replace("(","*(")
            a = a.replace("+ *(","+ (")
            a = a.replace("- *(","- (")
            a = a.replace("^*","^")
            a = a.replace("/ *","/")
            
            if a[0] == "*":
                a = a[1:]
                print("a =",a)
            
            #String Method to look for Exponents
            i = 0
            if a.count("^") > 0:
                while i < len(a):
                    carrot = a.find("^")
                    if carrot == -1:
                        break
                    print("carrot at index: ",carrot)
                    exp_right_side = a[carrot:]
                    print("exp_right_side",exp_right_side)
                    exp_right_space = exp_right_side.find(" ")
                    print("exp_right_space",exp_right_space)
                    if exp_right_space == -1:
                        exp_right_space = exp_right_side.rfind("")
                    print("exp_right_space",exp_right_space)
                    exp_right_side = a[carrot:carrot + exp_right_space]
                    print("right_side",exp_right_side)
                    exp_left_space = a[:carrot+1].rfind(" ")
                    print("left_side",exp_left_space)
                    if exp_left_space == -1:
                        exp_left_space = a[:carrot+1].find("")
                        print("left_side",exp_left_space)
                    exponent_range = a[exp_left_space:carrot + exp_right_space+1]
                    print("exp_range",exponent_range)
                    if exponent_range[:] == "-":
                        negative = exponent_range.find("-")
                        print("Negative",negative)
                        carrot_inner = exponent_range.find("^")
                        print("carrot_inner",carrot_inner)
                        exponent_left_range = exponent_range[negative:carrot_inner]
                        print("exponent_left_range",exponent_left_range)
                        exponent_left_sliced = "(" + exponent_left_range + ")"
                        exponent_range = exponent_range.replace(exponent_left_range,exponent_left_sliced)
                        print("exponent",exponent_range)
                    print("Exponent to be solved:",exponent_range)
                    exponent_range = exponent_range.replace("^","**")
                    evaled = str(eval(exponent_range))
                    exponent_range = exponent_range.replace("**","^").replace("(","").replace(")","")
                    replaced = a.replace(exponent_range,evaled)
                    print("replaced to a:",replaced)
                    print()
                    print()
                    
                    print("Exponent to Solve :       ",a[:exp_left_space],Back.GREEN,exponent_range,Style.RESET_ALL,a[carrot + exp_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Exponent Step : " , font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:exp_left_space] + '[color=33CAFF]' + exponent_range + '[/color]' + a[carrot + exp_right_space+1:],markup=True, font_size = 50, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    print()
                    print("Exponent Sovled :         ",a[:exp_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[carrot+exp_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Exponent Solved : " , font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:exp_left_space] + '[color=33CAFF]' + evaled + '[/color]' + a[carrot+exp_right_space+1:],markup=True, font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = 50, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    
                    a = replaced
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")
                    a = a.replace("^*","^")
                    a = a.replace("* (","(")
                    a = a.replace("(","*(")
                    a = a.replace("+ *(","+ (")
                    a = a.replace("- *(","- (")
                    a = a.replace("^*","^")
                    a = a.replace("/ *","/")
                    
                    if a[0] == "*":
                        a = a[1:]
                        print("a =",a)

                i = i + 1
            
            #String Method to look for Multiplication
            i = 0
            print(a)
            if a.count("*") > 0:
                while i < len(a):
                    a = a.replace(" * ","*")
                    print("mult",a)
                    found_mult = a.find("*")
                    if found_mult == -1:
                        break
                    print(found_mult)
                    mult_right_side = a[found_mult:]
                    print("mult_right_side",mult_right_side)
                    mult_right_space= mult_right_side.find(" ")
                    if mult_right_space == -1:
                        mult_right_space = mult_right_side.rfind("")
                    print("mult_right_found at index:",mult_right_space)
                    mult_left_side = a[:found_mult]
                    print("mult_left_side",mult_left_side)
                    mult_left_space = mult_left_side.rfind(" ")
                    if mult_left_space == -1:
                        mult_left_space = mult_left_side.find("")
                    print("mult_left_found at index:",mult_left_space)
                    mult_range = a[mult_left_space:found_mult + mult_right_space+1]
                    if mult_range == "":
                        break
                    print("mult_range",mult_range)
                    evaled = eval(mult_range)
                    print(evaled)
                    evaled = str(evaled)
                    evaled = evaled.replace("*"," * ")
                    replaced = a.replace(mult_range,evaled)
                    print("replaced to a:",replaced)
                    
                    if evaled.count("-") == 1:
                        evaled = "(" + evaled + ")"
                    
                    print()
                    print()
                    print("Multiplication to Solve : ",a[:mult_left_space],Back.GREEN,mult_range,Style.RESET_ALL,a[found_mult+mult_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Multiplication Step : " , font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:mult_left_space] + '[color=33CAFF]' + mult_range + '[/color]' + a[found_mult+mult_right_space+1:],markup=True , font_size = 50, size_hint_y= None, height=100))
                    
                    print()
                    print("Multiplication Solved :   ", a[:mult_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[found_mult+mult_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Multiplication Solved : ", font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:mult_left_space] + '[color=33CAFF]' + evaled + '[/color]'  + a[found_mult+mult_right_space+1:], markup=True, font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = 50, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    a = replaced
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")
                    a = a.replace("^*","^")
                    a = a.replace("* (","(")
                    a = a.replace("(","*(")
                    a = a.replace("+ *(","+ (")
                    a = a.replace("- *(","- (")
                    a = a.replace("^*","^")
                    a = a.replace("/ *","/")
                    
                    if a[0] == "*":
                        a = a[1:]
                        print("a =",a)
   
                i = i + 1
            
            #String Method to look for Division
            i = 0
            print(a)
            if a.count("/") > 0:
                while i < len(a):
                    a = a.replace(" / ","/")
                    print("div",a)
                    found_div = a.find("/")
                    if found_div == -1:
                        break
                    print(found_div)
                    div_right_side = a[found_div:]
                    print("div_right_side",div_right_side)
                    div_right_space= div_right_side.find(" ")
                    if div_right_space == -1:
                        div_right_space = div_right_side.rfind("")
                    print("div_right_found at index:",div_right_space)
                    div_left_side = a[:found_div]
                    print("div_left_side",div_left_side)
                    div_left_space = div_left_side.rfind(" ")
                    if div_left_space == -1:
                        div_left_space = div_left_side.find("")
                    print("div_left_found at index:",div_left_space)
                    div_range = a[div_left_space:found_div + div_right_space+1]
                    if div_range == "":
                        break
                    print("div_range",div_range)
                    evaled = eval(div_range)
                    print(evaled)
                    evaled = str(evaled)
                    evaled = evaled.replace("/"," / ")
                    replaced = a.replace(div_range,evaled)
                    print("replaced to a:",replaced)
                    
                    if evaled.count("-") == 1:
                        evaled = "(" + evaled + ")"

                    print()
                    print()
                    #print("Division to Solve : ",a[:div_left_space],Back.GREEN,div_range,Style.RESET_ALL,a[found_div+div_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Division Step : " , font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:div_left_space] + '[color=33CAFF]' + div_range + '[/color]' + a[found_div+div_right_space+1:],markup=True, font_size = 50, size_hint_y= None, height=100))
                    
                    print()
                    #print("Division Solved :   ", a[:div_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[found_div+div_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Division Solved : " , font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:div_left_space] + '[color=33CAFF]' + evaled + '[/color]' + a[found_div+div_right_space+1:],markup=True, font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = 50, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    a = replaced
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")
                    a = a.replace("^*","^")
                    a = a.replace("* (","(")
                    a = a.replace("(","*(")
                    a = a.replace("+ *(","+ (")
                    a = a.replace("- *(","- (")
                    a = a.replace("^*","^")
                    a = a.replace("/ *","/")
                    
                    if a[0] == "*":
                        a = a[1:]
                        print("a =",a)

                i = i + 1
            
            #String Method to look for Addition
            i = 0
            while i < len(a):
                if a.count("+") > 0:
                    a = a.replace(" + ","+")
                    print("add",a)
                    found_add = a.find("+")
                    if found_add == -1:
                        break
                    print('found_add',found_add)
                    add_left = a[:found_add]
                    print('add_left',add_left)
                    add_left_space = add_left.rfind(" ")
                    print('add_left_space',add_left_space)
                    if add_left_space == -1:
                        add_left_space = add_left.find("")
                        print('add_left_space',add_left_space)
                    add_right = a[found_add+1:]
                    print('add_right',add_right)
                    add_right_space = add_right.find(" ")
                    print('add_right_space',add_right_space)
                    if add_right_space == -1:
                        add_right_space = add_right.rfind("")
                        print('add_right_space',add_right_space)
                    add_range = a[add_left_space:found_add+add_right_space+1]
                    if add_range == "":
                        break
                    print('add_range',add_range)
                    evaled = eval(add_range)
                    print('evaled',evaled)
                    evaled = str(evaled)
                    replaced = a.replace(add_range,evaled)
                    print("replaced to a:",replaced)

                    print()
                    print()
                    #print("Addition to Solve :       ",a[:add_left_space],Back.GREEN,add_range,Style.RESET_ALL,a[found_add+add_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Addition Step : " , font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:add_left_space] + '[color=33CAFF]' + add_range + '[/color]' + a[found_add+add_right_space+1:],markup=True , font_size = 50, size_hint_y= None, height=100))
                    
                    print()
                    #print("Addition  Solved :        ",a[:add_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[found_add+add_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Addition Solved : " , font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:add_left_space] + '[color=33CAFF]' + evaled + '[/color]' + a[found_add+add_right_space+1:],markup=True , font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = 50, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    a = replaced
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")
                    a = a.replace("^*","^")
                    a = a.replace("* (","(")
                    a = a.replace("(","*(")
                    a = a.replace("+ *(","+ (")
                    a = a.replace("- *(","- (")
                    a = a.replace("^*","^")
                    a = a.replace("/ *","/")
                    
                    if a[0] == "*":
                        a = a[1:]
                        print("a =",a)

                i = i + 1
            
            #String Method to look for Subtraction
            i = 0 
            while i < len(a):
                if a.count("-") > 0:
                    a = a.replace(" - ","-")
                    print("sub",a)
                    found_sub = a.find("-")
                    if found_sub == -1:
                        break
                    print("found_sub",found_sub)
                    if found_sub == 0:
                        found_sub = a.rfind("-")
                    sub_left = a[:found_sub]
                    print("sub_left",sub_left)
                    if sub_left == "":
                        break
                    sub_left_space = sub_left.rfind(" ")
                    if sub_left_space == -1:
                        sub_left_space = sub_left.find("")
                        print("sub_left_space",sub_left_space)
                    sub_right = a[found_sub+1:]
                    print('sub_right',sub_right)
                    sub_right_space = sub_right.find(" ")
                    if sub_right_space == -1:
                        sub_right_space = sub_right.rfind("")
                        print("sub_right_space",sub_right_space)
                    sub_range = a[sub_left_space:found_sub+sub_right_space+1]
                    print("sub_range",sub_range)
                    if sub_range == "":
                        break
                    evaled = eval(sub_range)
                    print("evaled",evaled)
                    evaled = str(evaled)
                    replaced = a.replace(sub_range, evaled)
                    print("replaced to a:",replaced)
                    a = replaced
                    print("s",a)
 
                    print()
                    print()
                    #print("Subtraction to Solve :    ",a[:sub_left_space],Back.GREEN,sub_range,Style.RESET_ALL,a[found_sub+sub_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Subtraction Step : " , font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:sub_left_space] + '[color=33CAFF]'  + sub_range + '[/color]' + a[found_sub+sub_right_space+1:],markup=True , font_size = 50, size_hint_y= None, height=100))
                    
                    print()
                    #print("Subtraction  Solved :     ",a[:sub_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[found_sub+sub_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Subtraction Solved : " , font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:sub_left_space] + '[color=33CAFF]'  + evaled + '[/color]'  + a[found_sub+sub_right_space+1:],markup=True , font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = 50, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    a = replaced
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")
                    a = a.replace("^*","^")
                    a = a.replace("* (","(")
                    a = a.replace("(","*(")
                    a = a.replace("+ *(","+ (")
                    a = a.replace("- *(","- (")
                    a = a.replace("^*","^")
                    a = a.replace("/ *","/")
                    
                    if a[0] == "*":
                        a = a[1:]
                        print("a =",a)

                i = i + 1
            a = a.replace(" ","")
            a = a.replace("e - ","e-")
            
            #print Answer with commas
            a = float(a)
            a = format(a,",")
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print("Answer:                     ",a)
            self.ids.list_of_steps.add_widget(Label(text="Final Answer : ", font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= a, font_size = 50, size_hint_y= None, height=100))


        except Exception:
            try:
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
                    
            except Exception:               
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)  
                
#Quadratic
Builder.load_string("""
<Quadratic_Formula_Solver>
    id:Quadratic_Formula_Solver
    name:"Quadratic_Formula_Solver"
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
                text: "Quadratic Formula Calculator"
                
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
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1, 1
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        a.text = ""
                        b.text = ""
                        c.text = ""
                        list_of_steps.clear_widgets()    
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
            
                Label:
                    height: 250
                    font_size: 50
                    size_hint_y: None
                    padding: 5,5
                    text: "ax\u00B2 + bx + c = 0"
                
                Label:
                    height: 250
                    font_size: 50
                    size_hint_y: None
                    padding: 5,5
                    text:
                        '''      -b \u00B1 \u221A(b\u00B2 - 4ac)
                        x = -----------------------
                        '''      '''                2a'''    
            
            TextInput:
                id: a
                text: a.text
                multiline: False
                font_size: 125
                size_hint_y: None
                hint_text: "a ="
                height: 200
                padding: 10
                input_filter: lambda text, from_undo: text[:3 - len(a.text)]  
                    
                                                 
            TextInput:
                id: b
                text: b.text
                multiline: False
                hint_text: "b ="
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10          
                input_filter: lambda text, from_undo: text[:3 - len(b.text)]  
                
    
            TextInput:
                id: c
                text: c.text
                multiline: False
                hint_text: "c ="
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10          
                input_filter: lambda text, from_undo: text[:3 - len(c.text)]
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5  
    
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
                        Quadratic_Formula_Solver.steps(a.text + "," + b.text + "," + c.text)    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                  
                    
""")

class Quadratic_Formula_Solver(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Quadratic_Formula_Solver, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            print("Its working ESC = 27 LENGTH")
            return True

    def set_previous_screen(self):
        print("Length is almost working")        
        if sm.current != "Homepage":
            print("Its working List")
            sm.transition.direction = 'right'
            sm.current = "Menu"
            
    layouts = []
    def steps(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            entry_list =  entry.split(",")
            print("entry_list",entry_list)
            a = float(entry_list[0])
            b = float(entry_list[1])
            c = float(entry_list[2])
            
            #Check if ax^2 + bx + c = 0
            square = float(b*b - 4*a*c)
            print("square",square)
            
            if square > 0 :
                
                a = str(entry_list[0])
                b_out = "-" + str(entry_list[1])
                b_out = b_out.replace("--","")
                b = str(entry_list[1])
                c = str(entry_list[2])
                
                
                #POSITIVE
                self.ids.list_of_steps.add_widget(Label(text= "x1" ,font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " + \u221A(" + b + "\u00B2 - 4" + "(" + a + ")(" + c + "))" + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                
                ac = " - " + str(4*float(a)*float(c))
                ac = ac.replace("- -","+ ")
                b = str(float(b)**2)
                
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " + \u221A(" + b + ac + ")" + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " + \u221A(" + str(square) + ")" + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                
                squared = str(square**.5)
                print("squared",squared)
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " + " + squared + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                
                numer = str(float(b_out) + float(squared))
                self.ids.list_of_steps.add_widget(Label(text= "          " + numer + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                
                denom = str(2 * float(a))
                self.ids.list_of_steps.add_widget(Label(text= "          " + numer + "\nx = -------------------------------" + "\n                     " + denom ,font_size = 50, size_hint_y= None, height=300))
                
                answera = str(float(numer) / float(denom))
                print("answera",answera)
                self.ids.list_of_steps.add_widget(Label(text="x1 = " + answera ,font_size = 50, size_hint_y= None, height=150))
                self.layouts.append(layout)
                self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" ,font_size = 50, size_hint_y= None, height=150))
                
                a = str(entry_list[0])
                b_out = "-" + str(entry_list[1])
                b_out = b_out.replace("--","")
                b = str(entry_list[1])
                c = str(entry_list[2])
                
                #NEGATIVE
                self.ids.list_of_steps.add_widget(Label(text= "x2" ,font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " - \u221A(" + b + "\u00B2 - 4" + "(" + a + ")(" + c + "))" + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                
                ac = " - " + str(4*float(a)*float(c))
                ac = ac.replace("- -","+ ")
                b = str(float(b)**2)
                
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " - \u221A(" + b +  ac + ")" + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " - \u221A(" + str(square) + ")" + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                
                squared = str(square**.5)
                print("squared",squared)
                self.ids.list_of_steps.add_widget(Label(text= "        " + b_out + " - " + squared + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                
                numer = str(float(b_out) - float(squared))
                self.ids.list_of_steps.add_widget(Label(text= "          " + numer + "\nx = -------------------------------" + "\n                   2(" + a + ")" ,font_size = 50, size_hint_y= None, height=300))
                
                denom = str(2 * float(a))
                self.ids.list_of_steps.add_widget(Label(text= "          " + numer + "\nx = -------------------------------" + "\n                     " + denom ,font_size = 50, size_hint_y= None, height=300))
                
                answerb = str(float(numer) / float(denom))
                print("answerb",answerb)
                self.ids.list_of_steps.add_widget(Label(text="x1 = " + answerb ,font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" ,font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="FINAL ANSWER ",font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="x1 = " + answera,font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="x2 = " + answerb,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
            
            else:
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Square Root" ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
            
                            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
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
sm.add_widget(Domain_and_Range(name="Domain_and_Range"))     
sm.add_widget(Exponents_steps(name="Exponents_steps"))
sm.add_widget(FOIL(name="FOIL"))   
sm.add_widget(PEMDAS(name="PEMDAS"))
sm.add_widget(Quadratic_Formula_Solver(name="Quadratic_Formula_Solver"))	 
sm.add_widget(updates(name="updates"))
sm.current = "Homepage"   


class Algebra(App):
    def build(app):
        return sm

if __name__ == '__main__':
    Algebra().run()
