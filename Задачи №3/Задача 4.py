def bind_countries_to_capitals(countries, capitals):
    return dict(zip(countries, capitals))

print(bind_countries_to_capitals(["Bulgaria", "England", "Hungary"], ["Sofia", "London", "Budapest"]))