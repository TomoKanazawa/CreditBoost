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
        String updateQuery = "UPDATE loan SET amount = ?, duration = ? WHERE id = ?";
        int rowsAffected = jdbcTemplate.update(updateQuery, loan.getAmount(), loan.getDuration(), loan.getId());
        if (rowsAffected > 0) {
            return new ResponseEntity<>(loan, HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }

    @GetMapping("/{loanId}")
    public ResponseEntity<Loan> getLoanById(@PathVariable("loanId") long loanId) {
        String selectQuery = "SELECT * FROM loan WHERE id = ?";
        Loan loan = jdbcTemplate.queryForObject(selectQuery, new Object[]{loanId}, LoanController::mapLoan);
        if (loan != null) {
            return new ResponseEntity<>(loan, HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }

    @GetMapping
    public ResponseEntity<List<Loan>> getLoansByProfileId(@RequestParam("profileId") long profileId) {
        String selectQuery = "SELECT * FROM loan WHERE profileId = ?";
        List<Loan> loans = jdbcTemplate.query(selectQuery, new Object[]{profileId}, LoanController::mapLoan);
        if (!loans.isEmpty()) {
            return new ResponseEntity<>(loans, HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }

    private static Loan mapLoan(ResultSet rs, int rowNum) throws SQLException {
        Loan loan = new Loan();
        loan.setId(rs.getLong("id"));
        loan.setAmount(rs.getDouble("amount"));
        loan.setDuration(rs.getInt("duration"));
        // Set other loan properties if available in the loan table
        return loan;
    }
}
