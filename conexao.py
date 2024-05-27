import oracledb

class ConexaoBanco:

    def conexao_banco(user, senha):
        #conexao ao banco de dados oracle
        user = user
        passw = senha
        dsnStr = oracledb.makedsn("oracle.fiap.com.br", 1521, "ORCL")
        # Efetua a conexão com o Banco de Dados
        connection = oracledb.connect(user=user, password=passw, dsn=dsnStr)
        print("CONECTADO")
        return connection
    


