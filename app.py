from app.Search import Search
import click


@click.command()
@click.option('--name', prompt='Zadejte název článku ',
              help='Název článku na Wikipedii.')
def run(name):
    search = Search()

    while len(name) > 0:
        try:
            result = search.query(name)

            click.echo(result + "\n")
        except Error as e:
            click.echo(f"Při načítání článku s názvem '{name}' došlo k chybě:\n" + str(e), err=True)

        name = str(input('Zadejte název článku nebo stiskněte enter pro ukončení: '))


if __name__ == '__main__':
    run()
