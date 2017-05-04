class Spec:
    def __init__(self, input_spec, output_spec, spec_type):
        self.input_spec = input_spec
        self.output_spec = output_spec
        self.spec_type = spec_type

    def __str__(self):
        return "({}, {}, {})".format(self.input_spec,
                                     self.output_spec, self.spec_type)

    def match_suffix(self, test_case):
        a, b = test_case.input_file, test_case.output_file
        x, y = self.input_spec, self.output_spec
        return a.endswith(x) and b.endswith(y) and \
               a[0:len(a) - len(x)] == b[0:len(b) - len(y)]

    def match_prefix(self, test_case):
        a, b = test_case.input_file, test_case.output_file
        x, y = self.input_spec, self.output_spec
        return a.startswith(x) and b.startswith(y) and \
               a[len(x):] == b[len(y):]

    def match(self, test_case):
        if self.spec_type == '$':
            return self.match_suffix(test_case)
        if self.spec_type == '^':
            return self.match_prefix(test_case)
        raise AssertionError("spec_type must be '$' or '^'")

    def vowel_score(self):
        s = "aeiou"
        d1, d2 = {}, {}
        for i in range(len(s)):
            d1[s[i]] = self.input_spec.count(s[i])
            d2[s[i]] = self.output_spec.count(s[i])
        return (-d1['a'] - d1['e'] + d1['i'] - d1['o'] - d1['u']) + \
               (d2['a'] + d2['e'] - d2['i'] + d2['o'] + d2['u'])
