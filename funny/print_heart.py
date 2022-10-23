print('\n'.join([''.join([('ILovePython'[(x - y) % len('ILovePython')] if ((x * 0.05) ** 2 + (
            y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-32, 32)]) for y in
                 range(17, -17, -1)]))
