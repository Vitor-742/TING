def exists_word(word, instance):
    aux_list = []
    for i in range(len(instance)):
        aux_list.append({
            "palavra": word,
            "arquivo": instance.search(i)['nome_do_arquivo'],
            "ocorrencias": []
        })
        for ind, line in enumerate(instance.search(i)['linhas_do_arquivo']):
            if word.lower() in line.lower():
                aux_list[-1]['ocorrencias'].append({"linha": ind + 1})
        if len(aux_list[-1]['ocorrencias']) == 0:
            aux_list.pop()
    return aux_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
