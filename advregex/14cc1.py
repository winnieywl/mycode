print("\nCompiling Regular Expression Objects is very efficient.\n")
import re
hitchhiker = "The only person for whom the house was in any way special \
was Arthur Dent, and that was only because it happened to be the one he \
lived in. He had lived in it for about three years, ever since he had \
moved out of London because it made him nervous and irritable. He was \
about thirty as well, dark haired and never quite at ease with himself. \
The thing that used to worry him most was the fact that people always \
used to ask him what he was looking so worried about. He worked in local \
radio..."

mycomp = re.compile(r'd?a[rs]k')
hikerexample = mycomp.findall(hitchhiker)
print("The results of code customization 01:", hikerexample)
