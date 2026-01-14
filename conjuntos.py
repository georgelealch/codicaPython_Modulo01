def count_uniq_chars(list):
    result = []

    for uni in list:
        if uni not in result:
            result.append(uni)
    return len(result)

text2 = 'You know nothing Jon Snow'


print(count_uniq_chars(text2))


def build_HTML_list(coll):
  parts = []
  for item in coll:
    parts.append(f'<li>{item}</li>')

  inner_value = ''.join(parts)
  result = f'<ul>{inner_value}</ul>'
  return result

print(build_HTML_list('alex'))