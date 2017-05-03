class Spec:
    def __init__(self, input_spec, output_spec, spec_type):
        self.input_spec = input_spec
        self.output_spec = output_spec
        self.spec_type = spec_type

    def __str__(self):
        return "({}, {}, {})".format(self.input_spec,
                                     self.output_spec, self.spec_type)

    def match_suffix(self, test_case):
        A, B = test_case.input_file, test_case.output_file
        X, Y = self.input_spec, self.output_spec
        return A.endswith(X) and B.endswith(Y) and \
               A[0:len(A) - len(X)] == B[0:len(B) - len(Y)]

    def match_prefix(self, test_case):
        A, B = test_case.input_file, test_case.output_file
        X, Y = self.input_spec, self.output_spec
        return A.startswith(X) and B.startswith(Y) and \
               A[len(X):] == B[len(Y):]

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
