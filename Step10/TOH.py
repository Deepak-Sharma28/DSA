def fn(n,a,b,c):
    if n == 1:
        print("moved",n,"from",a,"to",c)
        return
    else:
        fn(n-1,a,c,b)
        print("moved",n,"from",a,"to",c)
        fn(n-1,b,a,c)
fn(3,"source","auxi","dest")


