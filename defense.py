import re
import csv
import argparse

def readFile(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text

def writeFile(path,text):
    file = open(path,"w")
    file.write(text)
    file.close()

def getCSV(path):
    result = []
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            result += row
    return result

def generateCondition(domains):
    result = []
    for domain in domains:
        domain = domain.strip()
        domain = domain.replace(".","\.")
        domain = domain.replace("*",".*")
        domain += "$"
        result.append(domain)
    condition = "referrer==self.location.hostname"
    for item in result:
        condition += ' || referrer.match("'+item+'")!=null'
    return condition

def generateWrapper(conditions):
    return '''let orig_f = EventTarget.prototype.addEventListener;
EventTarget.prototype.addEventListener = function(){
    if (arguments[0] == 'fetch'){
        let handler = arguments[1]
        arguments[1] = function(){
            let event = arguments[0];
            if (event.request.referrer){
                let referrer = (new URL(event.request.referrer)).host;
                if(''' + conditions +''')
                    return handler.apply(this,arguments)
            }
            //else it will be fetched from the network
        }
    }
    return orig_f.apply(this,arguments);
}

'''

def inputParser():
    desc = """
    This program can be used to add access control into Service Workers
    """
    parser = argparse.ArgumentParser(description=desc, epilog='Soroush Karami (skaram5@uic.edu)', prog='defense.py', usage='%(prog)s -w path_to_while_file -i path_to_js_file -o output_file')
    try:
        parser.add_argument('-w', '--white-list', type=str, nargs='?',help='the path of white list (CSV file)')
        parser.add_argument('-i', '--input', type=str, nargs='?',help='the path of input file')
        parser.add_argument('-o', '--output', type=str, nargs='?',help='the path of output file')
        args = parser.parse_args()
        return args.white_list,args.input,args.output,parser
    except:
        return None,None,None,parser

def main():
    csv,input_file,output_file,parser = inputParser()
    if not csv or not input_file or not output_file:
        print parser.print_help()
        return
    text = readFile(input_file)
    conditions = generateCondition(getCSV(csv))
    wrapper = generateWrapper(conditions)
    text = wrapper + text
    writeFile(output_file,text)
    print "The output is written to \'"+output_file+"\'"

main()
