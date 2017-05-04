


class LogicCircuit:

    def __init__(self, Gates, Wires):
        _Gates = np.array[Gate]
        _Wires = np.array[Wire]
        for g in Gates:
            _Gates.append(g)
        for w in Wires:
            _Wires.append(w)

    def connectCircuit:
        new_Gates = np.array[]
        new_Wires = np.array[]

        if (_Gates != null):
            for i in len(_Gates):
                g = Gate(_Gates.get(i))
                new_Gates.append(g)

        if (_Wires != null):
            for i in len(_Wires):
                w = Wire(_Wires.get(i))
                new_Wires.append(w)

        # Reconnect objects in memory for outgoing, from, and to wires

        # Outgoing is a wire from a gate
        for i in len(new_Gates):
            if (_Gates[i].Outgoing != null):
                int index = _Gates[i].Outgoing.Index
                for w in new_Wires:
                    if (w.Index == index):
                        new_Gates[i].Outgoing = w

        for i in len(new_Wires):
            # From is a gate
            if (_Wires[i].From != null):
                int index = _Wires[i].From.Index
                for g in new_Gates:
                    if (g.Index == index):
                        new_Wires[i].From = g
            # To is a gate
            if (_Wires[i].To != null):
                int index = _Gates[i].To.Index
                for w in new_Wires:
                    if (w.Index == index):
                        new_Gates[i].To = w

            # Next is a wire
            if (_Wires[i].Next != null):
                int index = _Wires[i].To.Index
                for w in new_Wires:
                    if (w.Index == index):
                        new_Wires[i].To = w

        _Gates = new_Gates
        _Wires = new_Wires

    def connectCircuitbyIndices(self):

        for g in self.get_Gates:

            for w in self.get_Wires:
                if (g.Outgoing_wire_index == w.Index):
                    g.Outgoing = w

            for x in g.get_variable_names:
                for w in g.get_variable_wires.get(x):
                    for g2 in this.get_Gates:
                        if (w.From_index == g2.Index):
                            w.From = g2
                        if (w.To_index == g2.Index):
                            w.To = g2

                    for w2 in this.get_Wires:
                        if (w.Next_index == w2.Index):
                            w.Next = w2

        for w in self.get_Wires:

            for g in self.get_Gates:
                if (w.From_index == g.Index):
                    w.From = g

                if (w.To_index == g.Index):
                    w.To = g

        for w1 in this.get_Wires:
            for w2 in this.get_Wires:
                if (w1.Next_index == w2.Index) && (w1.Next_index != -1):
                    w1.Next = w2
    
