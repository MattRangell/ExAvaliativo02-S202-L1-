class CLI:
    def __init__(self):
        self.teacher_crud = TeacherCRUD()
    
    def start(self):
        while True:
            print("========== MENU ==========")
            print("1. Criar Teacher")
            print("2. Ler Teacher")
            print("3. Atualizar CPF")
            print("4. Deletar Teacher")
            print("0. Sair")
            print("==========================")
            
            choice = input("Escolha uma opção: ")
            
            if choice == "1":
                name = input("Digite o nome do Teacher: ")
                ano_nasc = input("Digite o ano de nascimento do Teacher: ")
                cpf = input("Digite o CPF do Teacher: ")
                self.teacher_crud.create(name, ano_nasc, cpf)
                print("Teacher criado com sucesso!")
            
            elif choice == "2":
                name = input("Digite o nome do Teacher: ")
                teacher = self.teacher_crud.read(name)
                if teacher:
                    print(teacher)
                else:
                    print("Teacher não encontrado.")
            
            elif choice == "3":
                name = input("Digite o nome do Teacher: ")
                new_cpf = input("Digite o novo CPF do Teacher: ")
                self.teacher_crud.update(name, new_cpf)
                print("CPF atualizado com sucesso!")
            
            elif choice == "4":
                name = input("Digite o nome do Teacher: ")
                self.teacher_crud.delete(name)
                print("Teacher deletado com sucesso!")
            
            elif choice == "0":
                print("Encerrando o programa...")
                break
            
            else:
                print("Opção inválida. Digite novamente.")

cli = CLI()
cli.start()