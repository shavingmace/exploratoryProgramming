def borgesian_categorization(animal_seq):
    c_a=['챠우챠우']; c_b=['종이호랑이']; c_c=['개', '소','닭', '돼지', '말']
    c_d=['아기돼지']; c_e=['인어']; c_f=['봉황', '붕새', '용']
    c_g=['유기견', '주인이 죽은 개']; c_h=[]; c_i=['꿀오소리']
    c_j=['개미', '흰 개미']; c_k=['지네']; c_l=[]
    c_m=['고양이']; c_n=['꽃등에'];
    result = ['Borgesian Categorization: ']
    for elem in animal_seq:
        if elem in c_a:
            result.append(elem + ': ' + 'pertenecientes al Emperador 황제에 속하는 동물')
        elif elem in c_b:
            result.append(elem + ': ' + 'embalsamados 향료로 처리하여 박제로 보존된 동물')
        elif elem in c_c:
            result.append(elem + ': ' + 'amaestrados 사육동물')
        elif elem in c_d:
            result.append(elem + ': ' + 'lechones 젖을 빠는 돼지')
        elif elem in c_e:
            result.append(elem + ': ' + 'sirenas 인어')
        elif elem in c_f:
            result.append(elem + ': ' + 'fabulosos 전설상의 동물')
        elif elem in c_g:
            result.append(elem + ': ' + 'perros sueltos 주인없는 개')
        elif elem in c_h:
            result.append(elem + ': ' + 'incluidos en esta clasificaci n 이 분류에 포함되는 동물')
        elif elem in c_i:
            result.append(elem + ': ' + 'que se agitan como locos 광폭한 동물')
        elif elem in c_j:
            result.append(elem + ': ' + 'innumerables 셀 수 없는 동물')
        elif elem in c_k:
            result.append(elem + ': ' + 'dibujados con un pincel fin simo de pelo de camello 낙타털과 같이 미세한 털로 된 붓 으로 그릴 수 있는 동물')
        elif elem in c_l:
            result.append(elem + ': ' + 'etc tera 기타')
        elif elem in c_m:
            result.append(elem + ': ' + 'que acaban de romper el jarr n 물 주전자를 깨뜨리는 동물')
        elif elem in c_n:
            result.append(elem + ': ' + 'que de lejos parecen moscas 멀리서 볼 때 파리같이 보이는 동물')
        else:
            result.append(elem + ': ' + '?')
    return result

def printer(seq):
    for elem in seq:
        print(elem)

printer(borgesian_categorization(['벌', '봉황', '종이호랑이', '유기견', '닭', '고양이']))
