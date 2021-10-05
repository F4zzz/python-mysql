import mysql.connector
from mysql.connector import Error

db = mysql.connector.connect(host='localhost',database='tutorialyt',user='root',password='')
cursor= db.cursor()
if db.is_connected():
    cursor.execute('select database();')
    select_db = cursor.fetchone()
    print('Banco de dados: ',select_db)


def restart():
    valid = int(input('''Deseja realizar outra ação? 
    [1] Sim
    [2] Não
    -> '''))
    if valid == 1:
        main()
    else:
        print('Volte sempre :)')
        exit()

def main():
    menu = int(input('''O que deseja fazer? 
    [1] Ver os cadastros
    [2] Novo Cadastro
    [3] Excluir Cadastro
    [4] Mudar Cadastro
    -> '''))

    if menu == 1:
        try:
            sql_query='select * from users'
            cursor.execute(sql_query)
            users= cursor.fetchall()
            for user in users:
                print(f'ID: {user[0]} | Nome: {user[1]} | Idade: {user[2]} | Cor Favorita: {user[3]}')
        except Error as e:
            print('erro ao acessar a database', e)
        restart()

    if menu == 2:
        nome= input('Nome: ')
        idade= input('Idade: ')
        cor_favorita= input('Cor favorita: ')

        sql_query = f'''insert into users
        (nome, idade, cor_favorita)
        values 
        ("{nome}", "{idade}", "{cor_favorita}");'''

        try:
            cursor.execute(sql_query)
        except Error as e:
            print('Falha ao inserir dados ', e)
        restart()

    if menu == 3:

        try:
            sql_query = 'select * from users'
            cursor.execute(sql_query)
            users = cursor.fetchall()
            for user in users:
                print(f'ID: {user[0]} | Nome: {user[1]} | Idade: {user[2]} | Cor Favorita: {user[3]}')
            deleteuser = input('ID do cadastro que deseja apagar: ')
            deletecmd = f'delete from users WHERE id = "{deleteuser}";'
            cursor.execute(deletecmd)
            print(f'Cadastro apagado com sucesso!')
        except Error as e:
            print('erro ao acessar a database', e)
        restart()

    if menu == 4:

        try:
            sql_query = 'select * from users'
            cursor.execute(sql_query)
            users = cursor.fetchall()
            for user in users:
                print(f'ID: {user[0]} | Nome: {user[1]} | Idade: {user[2]} | Cor Favorita: {user[3]}')

            updateuser = input('ID do cadastro que deseja mudar: ')

            updatewhat = int(input('''O que deseja mudar no cadastro?
            [1] Nome
            [2] Idade
            [3] Cor Favorita
            -> '''))

            updatecmd = f'select * from users;'

            if updatewhat == 1:
                newupdate = input('Digite um novo Nome: ')
                updatecmd = f'update users set nome="{newupdate}" where id="{updateuser}";'
            elif updatewhat == 2:
                newupdate = input('Digite uma nova idade: ')
                updatecmd = f'update users set idade="{newupdate}" where id="{updateuser}";'
            elif updatewhat == 3:
                newupdate = input('Digite uma nova cor favorita: ')
                updatecmd = f'update users set cor_favorita="{newupdate}" where id="{updateuser}";'
            else:
                print('Opção inválida')
                restart()

            cursor.execute(updatecmd)
            print(f'Cadastro alterado com sucesso!')
        except Error as e:
            print('erro ao acessar a database', e)
        restart()


main()
