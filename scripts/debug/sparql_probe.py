"""Sonda temporária: testa consultas SPARQL ao Fedlex (roda no Actions)."""
import json, urllib.parse, urllib.request
EP = "https://fedlex.data.admin.ch/sparqlendpoint"
P = """PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
"""
def q(name, body):
    data = urllib.parse.urlencode({"query": P + body}).encode()
    req = urllib.request.Request(EP, data=data, headers={"Accept": "application/sparql-results+json"})
    try:
        res = json.load(urllib.request.urlopen(req, timeout=60))
        rows = res["results"]["bindings"]
        print(f"== {name}: {len(rows)} linhas")
        for r in rows[:8]:
            print("  ", {k: v["value"] for k, v in r.items()})
    except Exception as e:
        print(f"== {name}: ERRO {e}")
q("rs_notation", """SELECT ?act ?n WHERE { ?act jolux:classifiedByTaxonomyEntry ?e . ?e skos:notation ?n . FILTER(STR(?n) IN ("741.01","741.11","741.21")) } LIMIT 10""")
q("rs_notation_any", """SELECT ?s ?p ?n WHERE { ?s ?p ?n . FILTER(STR(?n) = "741.11") } LIMIT 10""")
for eli in ["1959/679_705_685", "1962/1364_1409_1420", "1979/1961_1961_1961"]:
    q("cons "+eli, f"""SELECT ?date ?url WHERE {{
 ?cons jolux:isMemberOf <https://fedlex.data.admin.ch/eli/cc/{eli}> .
 ?cons jolux:dateApplicability ?date .
 ?cons jolux:isRealizedBy ?expr .
 ?expr jolux:language <http://publications.europa.eu/resource/authority/language/FRA> .
 ?expr jolux:isEmbodiedBy ?m .
 ?m jolux:userFormat <https://fedlex.data.admin.ch/vocabulary/user-format/html> .
 ?m jolux:isExemplifiedBy ?url .
 FILTER(?date <= NOW()) }} ORDER BY DESC(?date) LIMIT 3""")
