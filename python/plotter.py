import matplotlib.pyplot as plt
import random

counter = 0

def count():
    global counter
    counter += 1

def lt(a,b):
    count()
    if a < b:
        return True
    else:
        return False

def eq(a,b):
    count()
    if a == b:
        return True
    else:
        return False

def plot(fs,n,title,type):
    global counter
    colors = ['r','g','b','c','m','y','k']
    fig, (axlin,axlog) = plt.subplots(1,2)
    fig.suptitle(title)
    fig.set_figwidth(15)
    for f_ind,f in enumerate(fs):
        nvals = list(range(n))
        cvals = list(range(n))
        for i in nvals:
            random.seed(i)
            counter = 0
            match type:
                case 'numeric':
                    f(nvals[i])
                case 'list':
                    l = random.sample(range(1,1000),nvals[i])
                    f(l)
                case 'search':
                    l = random.sample(range(1, 1000), nvals[i])
                    r = random.randint(1,1000)
                    f(l,r)
            cvals[i] = counter

        axlin.plot(nvals,cvals,color=colors[f_ind],label=f.__name__)
        axlin.set_title("Linear scale")
        axlin.set(ylabel="Comparisons used")
        axlin.legend()
        axlog.plot(nvals,cvals,color=colors[f_ind],label=f.__name__)
        axlog.set_yscale('log')
        axlog.set_title("Logarithmic scale")
        axlog.set(ylabel="Comparisons used")
        axlog.legend()
    plt.show()