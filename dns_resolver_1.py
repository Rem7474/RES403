import dns.resolver
types=["A","AAAA","MX","NS","SOA","TXT","CNAME"]
domain="iut-acy.local"
for type in types:
    try:
        result = dns.resolver.query(domain, type)
        print(f"{type} enregistrements pour {domain} :")
        for ipval in result:
            print(ipval.to_text())
    except:
        print("No",type,"record found for",domain)