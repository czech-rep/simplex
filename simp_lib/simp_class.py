import numpy as np

class Simp():
    '''
    class contain wraps all operations to optimize simplex table
    input:
    - a - np.array 
    - expr - list of expression coeficients
    '''
    def __init__(self, a: np.ndarray, expr: list):
        self.a = a.astype('float64')     # our np.array = simplex table
        self.num_vars = len(expr)      # number of original variables
        self.base = list(range(self.num_vars, a.shape[1]-1))                # numbers of additional variables = in base
        print(self.base)
        self._objective = expr + [0] * len(self.base)  # [x1, x2, .., 0, 0, ..] array of coeficients from objective

    def get_coefs(self):
        '''
        returns an array of coeficients from objective 
        of variables in base
        '''
        return [ self._objective[idx] for idx in self.base ]
       
    def current_maximum(self):
        '''
        get current function maximum, based on current coefs 
        '''
        coefs = self.get_coefs()
        resource = self.a[:,-1]
        return np.matmul(coefs, resource)

    def get_rel_profits(self):
        '''
        returns vector of relative profits:
        Z_objective - [ x_i * coef_objective ]
        '''
        coefs = self.get_coefs()
        Zj = [ np.matmul(self.a[:,i], coefs) for i in range( self.a.shape[1]-1 ) ] # exclude resource column

        return np.subtract( self._objective, Zj )
        # these two functions can merge
    def compare_profits(self, profits):
        '''
        choose index of the largest element - returns column index or None
        if all are equal or less than zero, end operation
        W  przypadku  maksymalizacji  funkcji  celu  do  kolejnego  rozwiązania  bazowego  wchodzi  zmienna  o największej wartości kryterium simpleks (czyli największej wartości w tzw. wierszu zerowym )
        '''
        print(profits)
        max_idx = np.argmax(profits)
        return max_idx if profits[max_idx] > 0 else None

    def based_to_replace(self, x_chosen):
        '''
        returns index of row
        which variable from base will be replaced
        decide by index of minimum positive coef: [resource] / [x_chosen]
        x_chosen - column index to be replaced
        '''
        resource = self.a[:,-1]
        column = self.a[:, x_chosen]

        with np.errstate(divide='ignore'):      # ignore warning (divide by zero may occur)
            vec = np.divide( resource, column )
            # vec[ vec==np.inf ] = np.nan         # inf convert to np.nan
        print(vec)
        try:
            res = np.nanargmin(np.where(vec > 0, vec, np.nan)) # minimum, from non np.nan
        except ValueError:
            return None
        return res      # throws All-NaN exception

    def rebuild_matrix(self, i, j): # i - row, j - column
        ''' 
        so, we want to insert new variable to base
        we know index of variable and its place
        we will have to normalize row where variable is incoming with value from crossing
        and substract it from other rows to zero the column of incoming
        '''
        a = self.a
        for rownum in range( a.shape[0] ):
            # for each row:
            if rownum == i:
                a[rownum] = a[rownum] / a[i,j]        # normalize row, now theres one in crossing
            else:
                a[rownum] = a[rownum] - a[i] / a[i,j] * a[rownum][j]   # substract row from others -> zeros in whole column

        return a

    def get_result(self):
        '''
        after optimization, return the final point coords
        returns python list
        '''
        result = np.empty(self.num_vars)
        resource = self.a[:,-1]

        for var in range(self.num_vars):
            result[var] = resource[ self.base.index(var) ] if var in self.base else 0
        
        return result.tolist()


    def optimize(self, show=False): # problem is our object
        '''
        function that iterates through steps to optimize our symplex matrix
        '''
        iterations = 1
        if show:
            print('expression: ', self._objective)
            print('at start: ', np.array_str(self.a, precision=3))

        
        while True:

            rel_profits = self.get_rel_profits()
            new_base = self.compare_profits(rel_profits) # var that enters base - column
            print('compare_profits: ', new_base)

            if new_base is None:
                # means no need for forther optimization
                break

            to_replace = self.based_to_replace(new_base) # var that exits base - row
            if to_replace is None:
                # means no need for forther optimization
                break
            
            self.base[to_replace] = new_base
            self.a = self.rebuild_matrix(to_replace, new_base) # matrix rebuild

            if show:
                np.set_printoptions(precision=2, )
                print(f'''
iteration {iterations}
{new_base} enters base at row {to_replace}
{self.a}
current max: {self.current_maximum()}
                ''')
            
            iterations += 1
            if iterations > 9999:
                break
                
        if show:
            print('optimization end')
            print('result: ', self.get_result())
            print('maximum value: ', self.current_maximum())

        return self.get_result(), self.current_maximum()