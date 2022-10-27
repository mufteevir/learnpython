def length_to_metric(imp_unit,met_unit,value):
    if imp_unit == 'inch':
        return inch_to_metric(met_unit,value)
    elif imp_unit == 'foot':
        return foot_to_metric(met_unit,value)
    elif imp_unit == 'yard':
        return yard_to_metric(met_unit,value)
    elif imp_unit == 'mile':
        return mile_to_metric(met_unit,value)
    elif imp_unit == 'hand':
        return hand_to_metric(met_unit,value)
        
def weight_to_metric(imp_unit,met_unit,value):
    if imp_unit == 'ounce':
        return ounce_to_metric(met_unit,value)
    elif imp_unit == 'pound':
        return pound_to_metric(met_unit,value)
    elif imp_unit == 'stone':
        return stone_to_metric(met_unit,value)
    elif imp_unit == 'short ton':
        return short_ton_to_metric(met_unit,value)
    elif imp_unit == 'long ton':
        return long_ton_to_metric(met_unit,value)
        
def temp_to_metric(imp_unit,met_unit,value):
    if imp_unit == 'Fahrenheit':
        return fahrenheit_to_metric(met_unit,value)  

def length_to_imperic(imp_unit,met_unit,value):
    if met_unit == 'millimeters':
        return millimeters_to_imperic(imp_unit,value)
    elif met_unit == 'meters':
        return meters_to_imperic(imp_unit,value)
    elif met_unit == 'kilometers':
        return kilometers_to_imperic(imp_unit,value)
        
def weight_to_imperic(imp_unit,met_unit,value):
    if met_unit == 'kilogram':
        return kilogram_to_imperic(imp_unit,value)
    elif met_unit == 'gram':
        return gram_to_imperic(imp_unit,value)
    elif met_unit == 'tonna':
        return tonna_to_imperic(imp_unit,value)
        
def temp_to_imperic(imp_unit,met_unit,value):
    if met_unit == 'Celsius':
        return celsius_to_imperic(imp_unit,value)
        
def inch_to_metric(met_unit,value):
    if met_unit == 'millimeters':
        return value*2.54
    elif met_unit == 'meters':
        return value*0.0254
    elif met_unit == 'kilometers':
        return value*0.0000254

def foot_to_metric(met_unit,value):
    if met_unit == 'millimeters':
        return value*304.8
    elif met_unit == 'meters':
        return value*0.3048
    elif met_unit == 'kilometers':
        return value*0.0003048
    
def yard_to_metric(met_unit,value):
    if met_unit == 'millimeters':
        return value*914.4
    elif met_unit == 'meters':
        return value*0.9144
    elif met_unit == 'kilometers':
        return value*0.0009144
    
def mile_to_metric(met_unit,value):
    if met_unit == 'millimeters':
        return value*1609344
    elif met_unit == 'meters':
        return value*1609.344
    elif met_unit == 'kilometers':
        return value*1.609344
    
def hand_to_metric(met_unit,value):
    if met_unit == 'millimeters':
        return value*101.6
    elif met_unit == 'meters':
        return value*0.1016
    elif met_unit == 'kilometers':
        return value*0.0001016
    
def ounce_to_metric(met_unit,value):
    if met_unit == 'kilogram':
        return value*0.028349523125
    elif met_unit == 'gram':
        return value*28.349523125
    elif met_unit == 'tonna':
        return value*0.000028349523125
    
def pound_to_metric(met_unit,value):
    if met_unit == 'kilogram':
        return value*0.45359237
    elif met_unit == 'gram':
        return value*453.59237
    elif met_unit == 'tonna':
        return value*0.00045359237
    
def stone_to_metric(met_unit,value):
    if met_unit == 'kilogram':
        return value*6.35029318
    elif met_unit == 'gram':
        return value*6350.29318
    elif met_unit == 'tonna':
        return value*0.00635029318
    
def short_ton_to_metric(met_unit,value):
    if met_unit == 'kilogram':
        return value*907.18474
    elif met_unit == 'gram':
        return value*907184.74
    elif met_unit == 'tonna':
        return value*0.90718474
    
def long_ton_to_metric(met_unit,value):
    if met_unit == 'kilogram':
        return value*1016.0469088
    elif met_unit == 'gram':
        return value*1016046.9088
    elif met_unit == 'tonna':
        return value*1.0160469088

def fahrenheit_to_metric(met_unit,value):
    if met_unit == 'Celsius':
        return value*9/5+32
    

def millimeters_to_imperic(imp_unit,value):
    if imp_unit == 'inch':
        return value*0.03937007874016
    elif imp_unit == 'foot':
        return value*0.003280839895013
    elif imp_unit == 'yard':
        return value*0.001093613298338
    elif imp_unit == 'mile':
        return value*6.213711922373e-7
    elif imp_unit == 'hand':
        return value*0.009842519685039
def meters_to_imperic(imp_unit,value):
    if imp_unit == 'inch':
        return value*39.37007874016
    elif imp_unit == 'foot':
        return value*3.280839895013
    elif imp_unit == 'yard':
        return value*1.093613298338
    elif imp_unit == 'mile':
        return value*0.0006213711922373
    elif imp_unit == 'hand':
        return value*9.842519685039
    
def kilometers_to_imperic(imp_unit,value):
    if imp_unit == 'inch':
        return value*39370.07874016
    elif imp_unit == 'foot':
        return value*3280.839895013
    elif imp_unit == 'yard':
        return value*1093.613298338
    elif imp_unit == 'mile':
        return value*0.6213711922373
    elif imp_unit == 'hand':
        return value*9842.519685039
        
def kilogram_to_imperic(imp_unit,value):
    if imp_unit == 'ounce':
        return value*35.27396194958
    elif imp_unit == 'pound':
        return value*2.204622621849
    elif imp_unit == 'stone':
        return value*0.1574730444178
    elif imp_unit == 'short ton':
        return value*0.001102311310924
    elif imp_unit == 'long ton':
        return value*0.0009842065276111
    
def gram_to_imperic(imp_unit,value):
    if imp_unit == 'ounce':
        return value*0.03527396194958
    elif imp_unit == 'pound':
        return value*0.002204622621849
    elif imp_unit == 'stone':
        return value*0.0001574730444178
    elif imp_unit == 'short ton':
        return value*0.000001102311310924
    elif imp_unit == 'long ton':
        return value*9.842065276111e-7

def tonna_to_imperic(imp_unit,value):
    if imp_unit == 'ounce':
        return value*35273.96194958
    elif imp_unit == 'pound':
        return value*2204.622621849
    elif imp_unit == 'stone':
        return value*157.4730444178
    elif imp_unit == 'short ton':
        return value*1.102311310924
    elif imp_unit == 'long ton':
        return value*0.9842065276111
        
def celsius_to_imperic(imp_unit,value):
    if imp_unit == 'Fahrenheit':
        return (value-32)*5/9