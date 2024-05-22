from django.http import HttpResponse


def table(request):
    rows = []
    for i in range(1, 11):
        for j in range(1, 11):
            if j == 1:
                res = f'<div>{i} x {j} = {i * j}<br>'
            elif j == 10:
                res = f'{i} x {j} = {i*j}</div><br><br>'
            else:
                res = f'{i} x {j} = {i * j}<br>'
            rows.append(res)
    return HttpResponse(f'<div style="display: flex; justify-content: space-around;">{''.join(rows)}</div>')

