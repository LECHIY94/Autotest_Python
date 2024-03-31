 import pytest
 from check_post import get_post, create_post

 id_check = 92054
 title_check = 'Казахский доктор Стрендж'


 def test_1(token):
     output = get_post(token)['data']
     res = []
     for item in output:
         res.append(item['id'])
     assert id_check in res


 def test_2(token):
     assert title_check.lower() in create_post(token)['title'].lower()





