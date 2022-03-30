# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


def home(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['account']
        return balanceSheet(request, pk)
    context = {
        'form': form
    }
    return render(request, 'checkbook/index.html', context)


def createAccount(request):
    form = AccountForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'checkbook/CreateNewAccount.html', context)


def balanceSheet(request, pk):
    account = get_object_or_404(Account, pk=pk)
    transactions = Transaction.transactions.filter(account=pk)
    currentTotal = account.initialDeposit
    tableContents = { }
    for t in transactions:
        if t.type == 'Deposit':
            currentTotal += t.amount
            tableContents.update({t: currentTotal})
        else:
            currentTotal -= t.amount
            tableContents.update({t: currentTotal})
    context = {
        'account': account,
        'tableContents': tableContents,
        'balance': currentTotal
    }
    return render(request, 'checkbook/BalanceSheet.html', context)


def addTransaction(request):
    form = TransactionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            pk = request.POST['account']
            form.save()
            return balanceSheet(request, pk)
    context = {
        'form': form,
    }
    return render(request, 'checkbook/AddTransaction.html', context)
