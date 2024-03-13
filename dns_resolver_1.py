# 3.2c - DNS Resolver
import dns.resolver
types=["A","AAAA","MX","NS","SOA","TXT","CNAME"]
domain="iut-acy.local"
for type in types:
    try:
        result = dns.resolver.resolve(domain, type)
        print(f"{type} enregistrements pour {domain} :")
        for ipval in result:
            print(f"  -{ipval.to_text()}")
        print("\n")
    except:
        print("No",type,"record found for",domain)