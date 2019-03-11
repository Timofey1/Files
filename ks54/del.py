from itertools import groupby

str = ":) :) :) ;) :) :\ :) >:( >:( >:) :3 Dx :) <3 :) :3 :3 =) >:( :\ >:( :3 :) %) :) xD :) >:) :3 =) :) ;( >:( ;( :) =) >:( >:( :) @_@ :3 =) :) :) :) =) >:( <3 :3 =) :) >;\ >:( :3 :) :F >:( 0 >:( xD :3 =) :) =) >:( :) :) :3 >:( ;( :3 =) >:( Dx :) <3 :) :3 :3 =) :) ;) :) :\ >:( >;\ >:( %) :3 =) :) Dx :) =) :) >:( >:( :F"
str = str.replace(" ", "")
print(str)
mas = str.split("")


print(mas)
shortlist = list(set(mas))
print(shortlist)
print(len(mas))

for i in shortlist:
    print(i)
    print(mas.count(i))
    print("--------------------------------------")

print(shortlist)