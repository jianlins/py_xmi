from cassis import *

with open('desc/type/pipeline_v1.xml', 'rb') as f:
    typesystem = load_typesystem(f)

with open('data/3_10646_r.txt.xmi', 'rb') as f:
   cas = load_cas_from_xmi(f, typesystem=typesystem)

for pna in cas.select('edu.utah.bmi.nlp.type.system.IND_PNEUMONIA'):
        print('Token: begin={0}, end={1}, text={2}'.format(pna.begin, pna.end, cas.get_covered_text(pna)))