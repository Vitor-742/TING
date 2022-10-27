from ting_file_management import file_management
import sys


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)['nome_do_arquivo'] == path_file:
            return
    file_read = file_management.txt_importer(path_file)
    obj_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_read),
        "linhas_do_arquivo": file_read
    }
    instance.enqueue(obj_file)
    sys.stdout.write(str(obj_file) + '\n')


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write('Não há elementos\n')
        return
    name_path_file = instance.dequeue()['nome_do_arquivo']
    sys.stdout.write(f'Arquivo {name_path_file} removido com sucesso\n')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
