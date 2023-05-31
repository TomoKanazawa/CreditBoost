import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.*;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/loans")
public class LoanController {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    @PostMapping
    public ResponseEntity<Loan> updateLoan(@RequestBody Loan loan) {
        String updateQuery = "UPDATE loan SET initial_loan_amnt = ?, num_installments = ?, total_amt_left = ? WHERE loan_id = ?";
        int rowsAffected = jdbcTemplate.update(updateQuery, loan.getInitialLoanAmount(), loan.getNumInstallments(), loan.getTotalAmountLeft(), loan.getLoanId());
        if (rowsAffected > 0) {
            return new ResponseEntity<>(loan, HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }

    @GetMapping("/{loanId}")
    public ResponseEntity<Loan> getLoanById(@PathVariable("loanId") long loanId) {
        String selectQuery = "SELECT * FROM loan WHERE loan_id = ?";
        Loan loan = jdbcTemplate.queryForObject(selectQuery, new Object[]{loanId}, LoanController::mapLoan);
        if (loan != null) {
            return new ResponseEntity<>(loan, HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }

    @GetMapping
    public ResponseEntity<List<Loan>> getLoansByProfileId(@RequestParam("profileId") long profileId) {
        String selectQuery = "SELECT * FROM loan WHERE profile_id = ?";
        List<Loan> loans = jdbcTemplate.query(selectQuery, new Object[]{profileId}, LoanController::mapLoan);
        if (!loans.isEmpty()) {
            return new ResponseEntity<>(loans, HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }

    private static Loan mapLoan(ResultSet rs, int rowNum) throws SQLException {
        Loan loan = new Loan();
        loan.setLoanId(rs.getLong("loan_id"));
        loan.setProfileId(rs.getLong("profile_id"));
        loan.setOpenStatus(rs.getBoolean("open_status"));
        loan.setInitialLoanAmount(rs.getDouble("initial_loan_amnt"));
        loan.setNumInstallments(rs.getInt("num_installments"));
        loan.setAmountPerInstallment(rs.getDouble("amt_per_installment"));
        loan.setTotalAmountLeft(rs.getDouble("total_amt_left"));
        return loan;
    }
}
