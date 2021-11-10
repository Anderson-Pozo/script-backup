from cmd import Cmd
from backup import execute_backup, execute_masive_backup, endpoints


class MyPrompt(Cmd):
    prompt = 'pb> '
    intro = "Bienvenido! Escriba ? para listar los comandos"

    def do_exit(self, inp):
        print("¡Adiós!")
        return True

    def do_help(self, arg: str):
        for index, value in enumerate(endpoints):
            print('{}. Generar respaldo de {}'.format(index + 1, value))
        print('8. Generar respaldo completo')
        print('9. Salir')

    def default(self, inp):
        if inp in [str(i + 1) for i, x in enumerate(endpoints)]:
            print(execute_backup(int(inp) - 1))
            return True
        elif inp == '8':
            print(execute_masive_backup())
        elif inp == '9':
            return self.do_exit(inp)
        else:
            print('Seleccione una opción válida')


if __name__ == '__main__':
    MyPrompt().cmdloop()
