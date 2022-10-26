from ting_file_management import file_management
import sys


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i) == path_file:
            return
    file_read = file_management.txt_importer(path_file)
    sys.stdout.write(str({
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_read),
        "linhas_do_arquivo": file_read
    }))
    instance.enqueue(path_file)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
