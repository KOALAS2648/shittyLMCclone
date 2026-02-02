labelsDict = {};
function getLabels(code, main_functions){
    for (var index=0; i <code.length; i++){
        var line = code[line];
        if (line[0] in main_functions){

        } else if( !(line[0] in main_functions) && !(line[1] == "DAT")){
        
            labelsDict[line[0]] = index;
            code[index].shift();
        }
    }
}

variablesDict = {};
function getVariables(code, main_functions){
    for (var index=0; i <code.length; i++){
        if (line[0] in main_functions){
            
        }
        else if( !(line[0] in main_functions) && (line[1] == "DAT")){
            variablesDict[line[0]] = index;
            code[index].shift();
        }
    }
}