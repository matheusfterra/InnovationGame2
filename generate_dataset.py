import random
import pandas as pd

pessoas=[]

list_color=[]
list_motivacao=[]
list_up=[]
list_sabor=[]

df_fem=pd.read_csv('datasets/ibge-fem-10000.csv')
df_mas=pd.read_csv('datasets/ibge-mas-10000.csv')
id=1


def generate_name():

    select_dataset= random.randint(0, 1)
    if select_dataset==0:
        df= df_mas
    else:
        df = df_fem

    list_names=df['nome']
    select_name_1 = random.randint(0, 9999)
    select_name_2 = random.randint(0, 9999)

    name1=list_names[select_name_1]
    name2=list_names[select_name_2]
    name=name1+" "+name2

    return(name)

def generate_cpf():
    cpf=""
    for i in range(0,11):
        cpf=cpf+str(random.randint(0,9))
    return(cpf)

def generate_state():
    url = 'https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_%C3%A1rea'
    df = pd.read_html(url)[0]
    estado=df['Unidade federativa']
    select_state=random.randint(0,26)
    return(estado[select_state])

def generate_idade():
    return(random.randint(18,48))

def generate_email(nome):
    nome=nome.replace(" ","").lower()
    servidor=['@hotmail.com','@yahoo.com.br','@gmail.com','@outlook.com','@bol.com']
    aleatory_servidor=random.randint(0,4)
    nome=nome+""+servidor[aleatory_servidor]
    return(nome)

def get_sabor():
    file = open('datasets/sabores.txt', 'r')
    Lines = file.readlines()
    file.close()
    list_sabor = []
    for line in Lines:
        list_sabor.append(line.replace("\n", ""))
    return(list_sabor)

def generate_sabor():
    global list_sabor
    select_sabor = random.randint(0, len(list_sabor)-1)

    return(list_sabor[select_sabor])

def get_color():
    file = open('datasets/cores.txt', 'r')
    Lines = file.readlines()
    file.close()
    list = []
    for line in Lines:
        list.append(line.replace("\n", ""))
    return(list)

def generate_color():
    global list_color
    select_color = random.randint(0, len(list_color)-1)

    return(list_color[select_color])

def get_motivacao():
    file = open('datasets/motivacao.txt', 'r')
    Lines = file.readlines()
    file.close()
    list = []
    for line in Lines:
        list.append(line.replace("\n", ""))
    return (list)

def generate_motivacao():
    global list_motivacao
    select_motivation = random.randint(0, len(list_motivacao)-1)

    return(list_motivacao[select_motivation])

def get_up():
    file = open('datasets/up.txt', 'r')
    Lines = file.readlines()
    file.close()
    list = []
    for line in Lines:
        list.append(line.replace("\n", ""))
    return(list)

def generate_up():
    global list_up
    select_up = random.randint(0, len(list_up)-1)

    return(list_up[select_up])

def start():
    global list_motivacao,list_color,list_sabor,list_up
    list_sabor = get_sabor()
    list_color = get_color()
    list_motivacao = get_motivacao()
    list_up = get_up()

def create_pessoa():
    global id
    pessoa=[]
    name=generate_name()
    pessoa.append(id)
    pessoa.append(name)
    pessoa.append(generate_cpf())
    pessoa.append(generate_state())
    pessoa.append(generate_idade())
    pessoa.append(generate_email(name))
    pessoa.append(generate_sabor())
    pessoa.append(generate_color())
    pessoa.append(generate_motivacao())
    pessoa.append(generate_up())
    pessoas.append(pessoa)
    id=id+1

def create_dataset(pessoas):
    df = pd.DataFrame(pessoas,columns=['ID','Nome', 'CPF','Estado','Idade','Email','Sabor','Cor','Motivacao','UP'])
    df=df.set_index(df.ID)
    del df['ID']
    return(df)

def loop(num):
    for i in range(0,num):
        create_pessoa()

def export_dataset():
    df=create_dataset(pessoas)
    df.to_csv("my_dataset.csv", index=False)
    #files.download("new_" + filename)
    print(df)


start()
loop(5)
export_dataset()